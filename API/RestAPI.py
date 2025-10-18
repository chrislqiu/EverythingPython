import requests

# Since we are getting a req from HTTP we want to convert to Python by using .json()

def avg_heartbeat(gender):
    url = "https://jsonmock.hackerrank.com/api/marathon"

    #start on page 1 of 400
    page = 1
    heart_rate = []

    while True:
        res = requests.get(f"{url}?page={page}&sex={gender}")
        data = res.json()
        
        #runner is now an object we need to access "avgheartbeat" of each runner
        for runner in data["data"]:
            heart_rate.append(runner["avgheartbeat"])

        if page >= data["total_pages"]:
            break

        page+=1

        if heart_rate:
            return sum(heart_rate) / len(heart_rate)
        else:
            return 0

print(f"The average heart rate of female runners is: " + str(avg_heartbeat("female")))
print(f"The average heart rate of male runners is: " + str(avg_heartbeat("male")))