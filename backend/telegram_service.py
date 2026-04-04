import requests

from config import *

def send(msg):

    try:

        url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

        data={

        "chat_id":CHAT_ID,

        "text":msg

        }

        requests.post(url,data=data)

    except Exception as e:

        print(e)