import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
URL = "https://api.nasa.gov/planetary/apod"

def apod_generator(url, api_key):
    params = {"api_key": api_key}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}