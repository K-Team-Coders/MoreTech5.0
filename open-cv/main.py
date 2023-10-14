from tracker.centroidtracker import CentroidTracker
from tracker.trackableobject import TrackableObject
from imutils.video import VideoStream
from itertools import zip_longest
from utils.mailer import Mailer
from imutils.video import FPS
from utils import thread
import numpy as np
import threading
import argparse
import datetime
import schedule
import imutils
from pathlib import Path
import time
import dlib
import json
import csv
import cv2
from loguru import logger


from celery.result import AsyncResult
from fastapi import Body, FastAPI, Form, Request,Header,Response,UploadFile, File
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

templates = Jinja2Templates(directory="templates")

origins = [
  "*"
]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
		"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
		"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
		"sofa", "train", "tvmonitor"]

start_time = time.time()

total_people=None

with open("utils/config.json", "r") as file:
    config = json.load(file)


with open("utils/args.json",'r') as file_args:
    args=json.load(file_args)


def log_data(move_in, in_time, move_out, out_time):
	# function to log the counting data
	data = [move_in, in_time, move_out, out_time]
	# transpose the data to align the columns properly
	export_data = zip_longest(*data, fillvalue = '')

	with open('utils/data/logs/counting_data.csv', 'w', newline = '') as myfile:
		wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
		if myfile.tell() == 0: # check if header rows are already existing
			wr.writerow(("Move In", "In Time", "Move Out", "Out Time"))
			wr.writerows(export_data)


model_caffe=Path().cwd().joinpath('detector').joinpath("MobileNetSSD_deploy.caffemodel")
model_proto=Path().cwd().joinpath('detector').joinpath("MobileNetSSD_deploy.prototxt")
logger.debug(model_caffe)
logger.debug(model_proto)

def get_frame(path_content):

	# load our serialized model from disk
    net = cv2.dnn.readNetFromCaffe(str(model_proto), str(model_caffe))
    if path_content == None:
        vs = cv2.VideoCapture(0)
    else:
        
        vs = cv2.VideoCapture(path_content)
    
	# if a video path was not supplied, grab a reference to the ip camera

	# initialize the video writer (we'll instantiate later if need be)
    writer = None

    # initialize the frame dimensions (we'll set them as soon as we read
    # the first frame from the video)
    W = None
    H = None

    # instantiate our centroid tracker, then initialize a list to store
    # each of our dlib correlation trackers, followed by a dictionary to
    # map each unique object ID to a TrackableObject
    ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
    trackers = []
    trackableObjects = {}

    # initialize the total number of frames processed thus far, along
    # with the total number of objects that have moved either up or down
    totalFrames = 0
    totalDown = 0
    totalUp = 0
    # initialize empty lists to store the counting data
    total = []
    move_out = []
    move_in =[]
    out_time = []
    in_time = []

    # start the frames per second throughput estimator
    fps = FPS().start()


    # loop over frames from the video stream
    while True:
        # grab the next frame and handle if we are reading from either
        # VideoCapture or VideoStream
        try:

            res,frame=vs.read()
    
            frame = cv2.resize(frame, (500,500))
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            

            # if the frame dimensions are empty, set them
            if W is None or H is None:
                (H, W) = frame.shape[:2]

            if args["output"] is not None and writer is None:
                fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                writer = cv2.VideoWriter(args["output"], fourcc, 30,
                    (W, H), True)

            status = "Waiting"
            rects = []

            # check to see if we should run a more computationally expensive
            # object detection method to aid our tracker
            if totalFrames % args["skip_frames"] == 0:
                # set the status and initialize our new set of object trackers
                status = "Detecting"
                trackers = []
                # convert the frame to a blob and pass the blob through the
                # network and obtain the detections
                blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)
                net.setInput(blob)
                detections = net.forward()

                # loop over the detections
                for i in np.arange(0, detections.shape[2]):
                    # extract the confidence (i.e., probability) associated
                    # with the prediction
                    confidence = detections[0, 0, i, 2]

                    # filter out weak detections by requiring a minimum
                    # confidence
                    if confidence > args["confidence"]:
                        # extract the index of the class label from the
                        # detections list
                        idx = int(detections[0, 0, i, 1])

                        # if the class label is not a person, ignore it
                        if CLASSES[idx] != "person":
                            continue

                        # compute the (x, y)-coordinates of the bounding box
                        # for the object
                        box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                        (startX, startY, endX, endY) = box.astype("int")

                        # construct a dlib rectangle object from the bounding
                        # box coordinates and then start the dlib correlation
                        # tracker
                        tracker = dlib.correlation_tracker()
                        rect = dlib.rectangle(startX, startY, endX, endY)
                        tracker.start_track(rgb, rect)

                        # add the tracker to our list of trackers so we can
                        # utilize it during skip frames
                        trackers.append(tracker)

            # otherwise, we should utilize our object *trackers* rather than
            # object *detectors* to obtain a higher frame processing throughput
            else:
                # loop over the trackers
                for tracker in trackers:
                    # set the status of our system to be 'tracking' rather
                    # than 'waiting' or 'detecting'
                    status = "Tracking"

                    # update the tracker and grab the updated position
                    tracker.update(rgb)
                    pos = tracker.get_position()

                    # unpack the position object
                    startX = int(pos.left())
                    startY = int(pos.top())
                    endX = int(pos.right())
                    endY = int(pos.bottom())

                    # add the bounding box coordinates to the rectangles list
                    rects.append((startX, startY, endX, endY))

            # draw a horizontal line in the center of the frame -- once an
            # object crosses this line we will determine whether they were
            # moving 'up' or 'down'
            cv2.line(frame, (0, H // 2), (W, H // 2), (0, 0, 0), 3)
            cv2.putText(frame, "-Prediction border - Entrance-", (10, H - ((i * 20) + 200)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        
            # use the centroid tracker to associate the (1) old object
            # centroids with (2) the newly computed object centroids
            objects = ct.update(rects)

            # loop over the tracked objects
            for (objectID, centroid) in objects.items():
                # check to see if a trackable object exists for the current
                # object ID
                to = trackableObjects.get(objectID, None)

                # if there is no existing trackable object, create one
                if to is None:
                    to = TrackableObject(objectID, centroid)

                # otherwise, there is a trackable object so we can utilize it
                # to determine direction
                else:
                    # the difference between the y-coordinate of the *current*
                    # centroid and the mean of *previous* centroids will tell
                    # us in which direction the object is moving (negative for
                    # 'up' and positive for 'down')
                    y = [c[1] for c in to.centroids]
                    direction = centroid[1] - np.mean(y)
                    to.centroids.append(centroid)

                    # check to see if the object has been counted or not
                    if not to.counted:
                        # if the direction is negative (indicating the object
                        # is moving up) AND the centroid is above the center
                        # line, count the object
                        if direction < 0 and centroid[1] < H // 2:
                            totalUp += 1
                            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                            move_out.append(totalUp)
                            out_time.append(date_time)
                            to.counted = True

                        # if the direction is positive (indicating the object
                        # is moving down) AND the centroid is below the
                        # center line, count the object
                        elif direction > 0 and centroid[1] > H // 2:
                            totalDown += 1
                            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                            move_in.append(totalDown)
                            in_time.append(date_time)
                            # if the people limit exceeds over threshold, send an email alert
                            if sum(total) >= 10: #config["Threshold"]
                                cv2.putText(frame, "-ALERT: People limit exceeded-", (10, frame.shape[0] - 80),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
                            to.counted = True
                            # compute the sum of total people inside
                            total = []
                            total.append(len(move_in) - len(move_out))

                # store the trackable object in our dictionary
                trackableObjects[objectID] = to

                # draw both the ID of the object and the centroid of the
                # object on the output frame
                text = "ID {}".format(objectID)
                cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.circle(frame, (centroid[0], centroid[1]), 4, (255, 255, 255), -1)
            # construct a tuple of information we will be displaying on the frame

            info_status = [
            ("Exit", totalUp),
            ("Enter", totalDown),
            ("Status", status),
            ]

            info_total=total_people= [
            ("Total people inside", ', '.join(map(str, total))),
            ]
            logger.debug(info_status)
            logger.error(info_total)
            # display the output
            for (i, (k, v)) in enumerate(info_status):
                text = "{}: {}".format(k, v)
                cv2.putText(frame, text, (10, H - ((i * 20) + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

            for (i, (k, v)) in enumerate(info_total):
                text = "{}: {}".format(k, v)
                cv2.putText(frame, text, (265, H - ((i * 20) + 60)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            # initiate a simple log to save the counting data
            if config["Log"]:
                log_data(move_in, in_time, move_out, out_time)

            # check to see if we should write the frame to disk
            if writer is not None:
                writer.write(frame)

            totalFrames += 1
            fps.update()

            # initiate the timer
            if config["Timer"]:
                # automatic timer to stop the live stream (set to 8 hours/28800s)
                end_time = time.time()
                num_seconds = (end_time - start_time)
                if num_seconds > 28800:
                    break


            fps.stop()
            
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
            
        except: StopIteration
        


import os
@app.get("/vid")
async def read_root(request: Request):
  return templates.TemplateResponse("index.html", context={"request": request})

@app.post("/vid/upload")
async def upload_file(file: UploadFile = File(...)):
    # Убедитесь, что у вас правильно настроен текущий рабочий каталог
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, "utils/data", file.filename)

    with open(file_path, 'wb') as image:
        content = await file.read()
        image.write(content)

    return StreamingResponse(get_frame(file_path),
                  media_type='multipart/x-mixed-replace; boundary=frame')

