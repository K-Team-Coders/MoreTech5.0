import os
import datetime
import time
import copy
import json
import random
from pathlib import Path
from typing import Optional, List
from math import radians, cos, sin, asin, sqrt 

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

results_office = []
for index, office in enumerate(offices):
    result = {}
    result["id"] = index
    result["name"] = office["salePointName"]
    result["address"] = office["address"]   
    result["openHours"] = office["openHours"]
    result["longitude"] = office["longitude"]
    result["latitude"] = office["latitude"]
    result["services"] = random.sample(list(timings.keys()), 10)
    results_office.append(result)


atms = 0
with open('atms.txt', 'r', encoding='utf-8') as f:
    atms = json.load(f) 

results_atms = []
for index, atm in enumerate(atms["atms"]):
    result = {}
    result["id"] = index 
    result["address"] = atm["address"]   
    result["longitude"] = atm["longitude"]
    result["latitude"] = atm["latitude"]
    result["services"] = atm["services"]
    results_atms.append(result)

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

# For calculating the distance in Kilometres  
def distance_1(La1, La2, Lo1, Lo2): 
      
    # The math module contains the function name "radians" which is used for converting the degrees value into radians. 
    Lo1 = radians(Lo1) 
    Lo2 = radians(Lo2) 
    La1 = radians(La1) 
    La2 = radians(La2) 
       
    # Using the "Haversine formula" 
    D_Lo = Lo2 - Lo1 
    D_La = La2 - La1 
    P = sin(D_La / 2)**2 + cos(La1) * cos(La2) * sin(D_Lo / 2)**2 
  
    Q = 2 * asin(sqrt(P)) 
     
    # The radius of earth in kilometres. 
    R_km = 6371 
       
    # Then, we will calculate the result 
    return(Q * R_km) 

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
    bank = random.choice([(x["name"], x["latitude"], x["longitude"]) for x in [y for y in results_office if service in y["services"]]])

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

    try:
        cur.execute("DELETE FROM queue WHERE timestamp < CURRENT_TIMESTAMP - service_time * INTERVAL '1 minute';")
        conn.commit()
    except Exception as e:
        logger.error(e)

@app.on_event("startup")
def start_modeling():
    scheduler = BackgroundScheduler()
    scheduler.add_job(modelingTalonAdded, "interval", seconds=1)
    scheduler.start()

def getAllTimings():
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
    unique_address = set([(x["address"], x["lattitude"], x["longitude"]) for x in preresult])
    result = []
    for address, lattitude, longitude in unique_address:
        timing = sum([x["service_time"] for x in preresult if x["address"] == address])
        result.append({
            "address": address,
            "lattitude": lattitude,
            "longitude": longitude,
            "time": timing
        })
    return result

@app.post("/getAllBanks")
def webAllBanks(lattitude: Optional[float] = 0.0, longitude: Optional[float] = 0.0, filter: Optional[str] = [], blind: Optional[bool] = None, immobile: Optional[bool] = None, backway: Optional[bool] = False):
    offices = []
    atms = results_atms
    # Чек на фильтры
    
    if filter:
        for subfilter in filter.split("//"):
            suboffice = [office for office in results_office if subfilter in office["services"]]
            offices = [office for office in suboffice if office not in offices]
    else:
        offices = results_office

    # Чек на инвалида
    if type(blind) != type(None):
        if blind:
            atms = [atm for atm in atms if atm["services"]["blind"]["serviceActivity"] == "AVAILABLE"]

    if type(immobile) != type(None):
        if immobile:
            atms = [atm for atm in atms if atm["services"]["wheelchair"]["serviceActivity"] == "AVAILABLE"]

    timings = getAllTimings()
    timings_addresses = [timing["address"] for timing in timings]
    timings_times = [timing["time"] for timing in timings]

    results_offices = []
    for office in offices:
        if office["name"] in timings_addresses:
            dicted = copy.deepcopy(office)
            dicted["timing"] = timings_times[timings_addresses.index(office["name"])]
            results_offices.append(dicted)

    cleaned_offices = []
    # Обработка координат
    for office in results_offices:
        if distance_1(lattitude, office["latitude"], longitude, office["longitude"]) < 10:
            cleaned_offices.append(office)

    cleaned_atms = []
    for atm in atms:
        if distance_1(lattitude, atm["latitude"], longitude, atm["longitude"]) < 10:
            cleaned_atms.append(atm)
    unique = []
    unique = [atm for atm in cleaned_atms if atm not in unique]


    return JSONResponse(content={"offices": cleaned_offices, "atms": unique}, status_code=200)
