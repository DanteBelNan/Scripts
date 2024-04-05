import requests as request
import json

url = "https://api.football-data.org/v4/"

response = request.get(url+"areas")

data = json.loads(response.text)


argId = 0
for area in data["areas"]:
    if area["name"] == "Argentina":
        #print(area)
        argId = area["id"]

response = request.get(url+"competitions/?areas="+str(argId))

data = json.loads(response.text)


compId = 0
for comp in data["competitions"]:
    #print(comp)
    if comp["name"] == "Liga Profesional":
        compId = comp["id"]
#print(compId)

response = request.get(url+"competitions/"+str(compId)+"/teams/?season=2023")
data = json.loads(response.text)


print(data["message"])
for info in data:
    print(info)

    