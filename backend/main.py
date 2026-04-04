from fastapi import FastAPI,UploadFile,File,BackgroundTasks

import shutil

import os

import time

from detector import FallDetector

from services import map_link,hospitals,firstaid

from telegram_service import send


app=FastAPI()

detector=FallDetector()

UPLOAD="uploads"

os.makedirs(UPLOAD,exist_ok=True)


def emergency_flow(conf):

    loc=map_link()

    aid=firstaid()

    send(f"""

FALL DETECTED

Confidence:{conf}

Location:

{loc}

FIRST AID:

{aid}

Checking condition...
""")


    time.sleep(10)


    send(f"""

10 SECOND ALERT

Person still down.

Location:

{loc}
""")


    time.sleep(50)


    hosp=hospitals()


    send(f"""

EMERGENCY

Person not responding.

Nearest hospitals:

{hosp}

Location:

{loc}
""")


@app.get("/")

def home():

    return {"status":"running"}


@app.post("/detect")

async def detect(

file:UploadFile=File(...),

background_tasks:BackgroundTasks=None

):

    try:

        path=os.path.join(UPLOAD,file.filename)

        with open(path,"wb") as buffer:

            shutil.copyfileobj(file.file,buffer)


        fall,conf=detector.detect(path)


        if not fall:

            return {"result":"no fall"}


        loc=map_link()

        aid=firstaid()

        hosp=hospitals()


        background_tasks.add_task(

        emergency_flow,

        conf

        )


        return{

        "confidence":conf,

        "location":loc,

        "aid":aid,

        "hospitals":hosp

        }


    except Exception as e:

        return {"error":str(e)}