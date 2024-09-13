from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import datetime
import csv

app = FastAPI()

origins = [
    "http://localhost:8899",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {'Hello':'n21'}


@app.get("/food")
def food(name:str):
    now = datetime.datetime.now()
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')

    file_path=os.path.join('code','data','food.csv')
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow('food','time')


    with open(file_path, mode='a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, current_time])

    return {"food":name, "time": current_time}
