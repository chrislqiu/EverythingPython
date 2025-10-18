import requests

# Since we are getting a req from HTTP we want to convert to Python by using .json()

def avg_heartbeat(gender):
    url = "https://jsonmock.hackerrank.com/api/marathon"

    #start on page 1 of 400
    page = 1
    heart_rate = []

    #while True:
    res = requests.get(f"{url}?page={page}&sex={gender}")
    data = res.json()

    print(data)

print(avg_heartbeat("female"))