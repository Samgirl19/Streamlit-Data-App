import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
URL = "https://api.nasa.gov/planetary/apod"

def apod_generator():
    params = {"api_key": NASA_API_KEY}

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}