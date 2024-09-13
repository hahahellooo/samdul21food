from typing import Union
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8899",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_path=os.expanduser('~')
file_path=os.path.join(user_path,'code','data','food.csv')
if not os.exists(file_path):
    os.makedirs(os.path.dirname(file_path), exist=ok=True)
    with open(file_path, mode='w', encoding='utf--8') as f:
        writer = csv.writer(f)
        writer.writerow['food','time']


@app.get("/")
def read_root():
    return {'Hello':'n21'}

@app.get("/food")
def food(name:str):
    current_time = datetime.now()strftime('%Y-%m-%d %H:%M:%S')

    with open(file_path, mode='a', encodinf='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, currnet_time])

    return {"food":name, "time": current_time}


