import os
import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.environ.get("NASA_API_KEY")
url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2020-07-01&api_key={KEY}"

def NasaImg():
    print(url)
    res = requests.get(url)
    data = res.json()

    return data

print(NasaImg())
