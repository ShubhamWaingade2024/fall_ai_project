
import requests
from config import *
from openai import OpenAI


def map_link():

    try:

        link=f"https://www.google.com/maps?q={LAT},{LON}"

        return link

    except:

        return "Location unavailable"


def hospitals():

    try:

        url=f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LAT},{LON}&radius=3000&type=hospital&key={GOOGLE_KEY}"

        response=requests.get(url)

        data=response.json()

        hospital_list=[]

        if "results" in data:

            for place in data["results"][:5]:

                name=place["name"]

                address=place.get("vicinity","")

                hospital_list.append(f"{name} - {address}")

        return hospital_list

    except Exception as e:

        print(e)

        return ["Hospital API error"]


def firstaid():

    try:

        client=OpenAI(api_key=OPENAI_KEY)

        prompt="""
A person has fallen and is unconscious.

Give short emergency first aid steps for nearby people.
Keep it simple.
"""

        response=client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                {"role":"system","content":"You are a first aid assistant."},

                {"role":"user","content":prompt}

            ]

        )

        text=response.choices[0].message.content

        return text

    except Exception as e:

        print(e)

        return "Call emergency services. Check breathing. Keep person safe."