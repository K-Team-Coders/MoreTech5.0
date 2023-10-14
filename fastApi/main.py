import os
import datetime
import time
import json
import random
from pathlib import Path

import psycopg2
from loguru import logger
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

timings = {
    "Кредит наличными": 7.6,
    "Экспресс-кредит": 4.5,
    "Рефинансирование": 8.9,
    "Кредит под залог недвижимости": 10.9,
    "Дебетовые карты": 7.3,
    "Кредитные карты": 4.5,
    "Пенсионные карты": 8.9,
    "Карты жителя": 5.7,
    "Социальные карты":12.3,
    "Ипотека на готовый дом": 10.1,
    "Ипотека на строящийся дом": 13.8,
    "Кредит под залог имеющейся недвижимости": 7.8,
    "Ипотека на машино-места и кладовки": 9.8,
    "Ипотека с материнским капиталом": 7.8,
    "Вклады": 9.8,
    "Операции по счету": 8.2,
    "Операции по инвестициям": 6.2,
    "Обмен валют": 8.1,
    "Оплата ЖКХ": 9.1,
    "Расчетный счет": 5.6,
    "Регистрация бизнеса": 9.5,
    "Кредиты": 5.6,
    "Бизнес-карты": 8.7,
    "Эквайринг": 14.1,
    "Депозиты": 12.1,
    "ВЭД": 7.8,
    "Гарантии и аккредитивы": 12.1,
    "Сервисы для бизнеса": 9.2
}

PRODUCTION = False

offices = 0
with open('offices.txt', 'r', encoding='utf-8') as f:
    offices = json.load(f) 

atms = 0
with open('atms.txt', 'r', encoding='utf-8') as f:
    atms = json.load(f) 

DBenv = Path().cwd().parent.joinpath("DB.env")
load_dotenv(DBenv, override=True)

conn = 0
cur = 0

logger.debug("Waiting for DB service Up...")
time.sleep(5)

try:     
    HOST = None
    DBNAME = None
    PASSWORD = None

    if PRODUCTION:
        HOST=os.environ.get("DB_HOST")  
        DBNAME=os.environ.get("POSTGRES_DB")
        USER=os.environ.get("POSTGRES_USER")
        PASSWORD=os.environ.get("POSTGRES_PASSWORD")
    else:
        HOST=os.environ.get("DB_LOCAL")
        DBNAME=os.environ.get("LOCAL_DB")
        USER=os.environ.get("LOCAL_USER")
        PASSWORD=os.environ.get("LOCAL_PASSWORD")
    
    PORT=os.environ.get("PORT")

    logger.success(f'Database connection started {HOST}, {PORT}, {DBNAME}, {USER}, {PASSWORD}, - env variables!')

    conn = psycopg2.connect(
        dbname=DBNAME, 
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        port=PORT)

    cur = conn.cursor()

    if PRODUCTION:
        logger.success('Docker DB connected!')
    else:
        logger.success('Local DB connected!')

except Exception as e:
    logger.error(f'Database connect failed \n {e}!')


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def bankAvaiability():

def modelingTalonAdded():
    """
    Каждые N секунд добавляется человек в очередь в рандомное отделение
    Случайно выбирается отделение, случайно выбирается услуга
    Для каждой услуги предложено свое время (в соответсвии с реальными историческими данными)
    Через M секунд талончик обслуживается и удаляется из временной БД.
    """
    service = random.choice(list(timings.keys()))
    service_time = timings[service]
    current_time = datetime.datetime.now()
    bank = random.choice([(x["salePointName"], x["latitude"], x["longitude"]) for x in offices])

    logger.debug(f"Талон -- {service} {service_time}")
    logger.debug(f"Время получения талона -- {current_time}")
    logger.debug(f"Отделение -- {bank[0]}")
    logger.debug(f"Координаты -- {bank[1]} - {bank[2]}")

    try:
        cur.execute("INSERT INTO queue (service_time, service, timestamp, address, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s);", (service_time, service, current_time, bank[0], bank[1], bank[2]))
        conn.commit()
    except Exception as e:
        logger.error(e)
        conn.rollback()

@app.on_event("startup")
def start_modeling():
    scheduler = BackgroundScheduler()
    scheduler.add_job(modelingTalonAdded, "interval", seconds=5)
    scheduler.start()

@app.get("/videocam")
def videocam(item: UploadFile):
    pass

def getAtmsCoords():
    results = []
    for index, atm in enumerate(atms["atms"]):
        result = {}
        result["id"] = index 
        result["address"] = atm["address"]   
        result["longitude"] = atm["longitude"]
        result["latitude"] = atm["latitude"]
        results.append(result)
    return results

def getOfficesCoords():
    results = []
    for index, office in enumerate(offices):
        result = {}
        result["id"] = index
        result["name"] = office["salePointName"]
        result["address"] = office["address"]   
        result["openHours"] = office["openHours"]
        result["longitude"] = office["longitude"]
        result["latitude"] = office["latitude"]
        result["services"] = random.sample(list(timings.keys()), 10)
        results.append(result)
    return results

@app.post("/addQueue")
def addQueue(id: int, queue: int):
    cur.execute()

@app.get("/getAllBanks")
def webAllBanks():
    offices = getOfficesCoords()
    atms = getAtmsCoords()
    return JSONResponse(content={"offices": offices, "atms": atms}, status_code=200)

@app.get("/getAllTimings")
def allTimings():
    cur.execute("SELECT * FROM queue")
    data = cur.fetchall()

    preresult = []
    for index, subdata in enumerate(data):
        data = {
            "service_time": subdata[1],
            "address": subdata[4],
            "lattitude": subdata[5],
            "longitude": subdata[6]
        } 
        preresult.append(data)

    unique_address = set([x["address"] for x in preresult])
    result = []
    for address in unique_address:
        timing = sum([x["service_time"] for x in preresult])
        result.append({
            "address": address,
            "time": timing
        })

    return JSONResponse(status_code=200, content={"data": result})