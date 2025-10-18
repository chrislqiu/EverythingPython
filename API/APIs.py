import requests
import os

NASA_API_KEY = os.environ.get("NASA_API_KEY")
randUser = "https://randomuser.me/"
NASA = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={NASA_API_KEY}"

def NasaImg():
    res = requests.get(NASA)
    data = res.json()

    print(data)