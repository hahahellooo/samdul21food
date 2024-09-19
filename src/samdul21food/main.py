from typing import Union
from fastapi import FastAPI
import pymysql.cursors
from fastapi.middleware.cors import CORSMiddleware
import os
import datetime
import csv
from datetime import datetime
from pytz import timezone

app = FastAPI()

origins = [
    "http://localhost:8899",
    "https://samdul21food.web.app"
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
    hi=datetime.now(timezone('Asia/Seoul'))
    current_time = hi.strftime('%Y-%m-%d %H:%M:%S')

    connection = pymysql.connect(host=os.getenv("DB_IP", "localhost"),
                                 user='food',
                                 password='1234',
                                 port=int(os.getenv("DB_PORT","33306")),
                                 database='fooddb',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `foodhistory`(username, foodname,dt) VALUES (%s, %s, %s)"
            cursor.execute(sql,("n21", name, current_time))
            result = cursor.fetchone()
            print(result)
        connection.commit()


    file_path=os.getenv("FILE_PATH",f"{os.getenv('HOME')}/tmp/foodcsv/food.csv")
    dir_path=os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    if not os.path.exists(file_path):
        with open(file_path, mode='w', encoding='utf-8',  newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['food','time'])


    with open(file_path, mode='a', encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, current_time])

    return {"food":name, "time": current_time}
