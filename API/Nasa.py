import os
import requests

KEY = os.environ.get("NASA_API_KEY")
url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={KEY}"

def NasaImg():
    res = requests.get(url)
    data = res.json()

    return data

print(NasaImg())
