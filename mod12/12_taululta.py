import requests
import json # laittaa jsonin luettavampaan muotoon. Ei tule yhtenä pötkönä


hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyyntö).json() # .json käänytää pyynnön luettavaksi
#tämä on lähinnä koko vastauksen käsittelyä varten
print(json.dumps(vastaus, indent=2))

sanakirja = vastaus[0]
for a in vastaus:
    print(a["show"]["name"])



