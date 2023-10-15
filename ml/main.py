import os
import pandas as pd
import numpy as np
from pathlib import Path
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
import scipy.stats as scs
from fastapi import FastAPI
from io import BytesIO
from typing import List,Any
from celery.result import AsyncResult
from fastapi import Body, FastAPI, Form, Request,Header,Response,UploadFile, File
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from loguru import logger
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import json


class PredictionData(BaseModel):
    param1: str
    param2: str


app=FastAPI()
templates = Jinja2Templates(directory="templates")

def getyour_xls(path:str):
    df_dirt=pd.read_excel(path)
    df=df_dirt[['date','visiters']]
    df = df.set_index('date')
    df=df.loc[df['visiters'] != 'close']
    df.index = pd.to_datetime(df.index)
    df["hour"] = df.index.hour
    df["weekday"] = df.index.weekday
    df['is_weekend'] = df.weekday.isin([5,6])*1
    df=df.dropna()
    return df

def fill_dataframe(df, start_date, end_date, frequency='M', value=0):
    """
    """
    date_range = pd.date_range(start=start_date, end=end_date, freq=frequency)
    for date in date_range:
        if date not in df.index:
            df.loc[date] = value

def code_mean(data, cat_feature, real_feature):
    """
    """
    return dict(data.groupby(cat_feature)[real_feature].mean())

def prepareData(data, split_date, lag_start=5, lag_end=20, test_size=0.15):

    data = pd.DataFrame(data.copy())

    # добавляем лаги исходного ряда в качестве признаков
    for i in range(lag_start, lag_end):
        data["lag_{}".format(i)] = data.visiters.shift(i)

    data["hour"] = data.index.hour
    data["weekday"] = data.index.weekday
    data['is_weekend'] = data.weekday.isin([5, 6]) * 1

    # считаем средние только по тренировочной части, чтобы избежать лика
    data['weekday_average'] = data['weekday'].map(code_mean(data.loc[:split_date], 'weekday', "visiters"))
    data["hour_average"] = data['hour'].map(code_mean(data.loc[:split_date], 'hour', "visiters"))

    # выкидываем закодированные средними признаки
    data.drop(["hour", "weekday"], axis=1, inplace=True)

    data = data.dropna()
    
    # разбиваем весь датасет на тренировочную и тестовую выборку
    X_train = data.loc[data.index <= split_date].drop(["visiters"], axis=1)
    y_train = data.loc[data.index <= split_date]["visiters"]
    X_test = data.loc[data.index > split_date].drop(["visiters"], axis=1)
    y_test = data.loc[data.index > split_date]["visiters"]

    return X_train, X_test, y_train, y_test



@app.post("/test")
async def get_pred(data: PredictionData):
    # Убедитесь, что у вас правильно настроен текущий рабочий каталог
    file_path = Path().cwd().joinpath('data').joinpath('cumForJora.xlsx')
    logger.debug(file_path)

    param1 = data.param1
    param2 = data.param2

    
    data_file=(getyour_xls(file_path))
    fill_dataframe(data_file,param1,param2,"15T")
    # logger.debug(data_file)
    X_train, X_test, y_train, y_test = prepareData(data_file,split_date=param1 ,
                                                   test_size=0.3, lag_start=12, lag_end=48)
    lr = RandomForestRegressor()
    lr.fit(X_train, y_train)
    prediction = lr.predict(X_test).tolist()
    json_pred = json.dumps(prediction)
    json_time=json.dumps(X_test.index.strftime('%Y-%m-%d %H:%M:%S').tolist())
    return {"pred":json_pred,"time":json_time}


@app.get("/xls")
async def read_root(request: Request):
  return templates.TemplateResponse("index.html", context={"request": request})

# ____________________________________
@app.post("/xls/upload/{start}/{stop}")
async def upload_file(start:str,stop:str,file: UploadFile = File(...)):
    # Убедитесь, что у вас правильно настроен текущий рабочий каталог
    file_path = Path.cwd().joinpath(file.filename)
    
    # Сохраните загруженный файл в папку "data"
    with open(file_path, "wb") as f:
       f.write(file.file.read())

    # Прочтите сохраненный файл и создайте DataFrame
    df = pd.read_excel(file_path)

    # Создайте буфер для записи в него данные DataFrame
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)


    param1 = start
    param2 = stop
    logger.error(param1)
    
    data_file=(getyour_xls(file_path))
    logger.debug(data_file)
    fill_dataframe(data_file,param1,param2,"15T")
    logger.debug(fill_dataframe(data_file,param1,param2,"15T"))
    X_train, X_test, y_train, y_test = prepareData(data_file,split_date=param1 ,
                                                   test_size=0.3, lag_start=12, lag_end=48)
    # logger.error(X_test)
    # logger.debug(y_test)
    lr = RandomForestRegressor()
    lr.fit(X_train, y_train)
    prediction = lr.predict(X_test).tolist()
    json_pred = json.dumps(prediction)
    json_time=json.dumps(X_test.index.strftime('%Y-%m-%d %H:%M:%S').tolist())
    return {"pred":json_pred,"time":json_time}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5000,reload=True)