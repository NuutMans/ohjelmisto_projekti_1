import json
import requests

city_name = input("Anna kaupungin nimi: ")
API_key = "dcca942af5159828b13cf8de735cfe67"
lang = "fi"
lat = ""
lon = ""

pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_key}"

try:
    vastaus = requests.get(pyyntö)
    #print ("Status code: ", vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        #print(json.dumps(data, indent=2))
        eka = data[0]
        #print(eka)
        lat, lon, = eka["lat"], eka["lon"]
        print(f"Kaupungin {city_name} leveysaste on {lat} ja pituusaste {lon}")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")


# tämä tehdään kun geocoding api palauttaa ensin lat ja lon

pyyntö2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"

try:
    vastaus = requests.get(pyyntö2)
    #print ("Status code: ", vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        #print(json.dumps(data, indent=2))
        print(f"Sää kohteessa {city_name} on {data["weather"][0]["description"]}")
        print (f"Lämpötila kohteessa {city_name} on {data["main"]["temp"]}°C")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")


#TODO
# kysyy paikkakunnan nimen
# tulostaa siitä vastaavan säätilan tekstin
# lämpötilan Celsius-asetina




