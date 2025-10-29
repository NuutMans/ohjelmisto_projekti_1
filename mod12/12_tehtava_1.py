import json
import requests

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    print ("Status code: ", vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print("Tässä on satunnainen Chuck Norris vitsi:")
        print(json.dumps(data["value"], indent=2))

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")