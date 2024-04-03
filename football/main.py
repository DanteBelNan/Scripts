import requests as request
import json

url = "https://api.football-data.org/v4/"

response = request.get(url+"areas")

data = response.text

data = json.loads(data)

print (data["count"])

for area in data["areas"]:
    if area["name"] == "Argentina":
        print(area)
    
    