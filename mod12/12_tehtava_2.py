import json
import requests

city_name = input("Anna kaupungin nimi: ")
API_key = "dcca942af5159828b13cf8de735cfe67"
lang = "fi"


pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang={lang}"

try:
    vastaus = requests.get(pyyntö)
    print ("Status code: ", vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        print(f"Sää kohteessa {city_name} on {data["weather"][0]["description"]}")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")