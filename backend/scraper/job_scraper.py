import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

def get_jobs_from_adzuna(keyword):
    url = f"https://api.adzuna.com/v1/api/jobs/de/search/1"
    
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": keyword,
        "where": "Deutschland",
        "results_per_page": 20
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Fehler:", response.status_code)
        return None

if __name__ == "__main__":
    jobs = get_jobs_from_adzuna("Python Developer")
    
    if jobs:
        print("Jobs gefunden!")
        print("Anzahl:", jobs["count"])
    else:
        print("Keine Jobs gefunden!")