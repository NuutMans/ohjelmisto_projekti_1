# mod07 monikko
import random

# monikko eli (tuple) on "kuin lista jota ei voi muokata"

lista = [1, 2, 3, 4, 5]
print(lista)

monikko = (1,2, 3, 4, 5, 6)
print (monikko)
# monikon voi luoda ilman kaarisulkeita
monikko2 = 1, 2, 3, 4, 5
print(monikko2)

# monikko voi sisältää erilaista tietoa
monikko3 = (1, 2, "nuutti", (3, 4), 88)
print(monikko3)

# luetaan listan eka alkio
print(lista[0])
print (monikko[0])

# Toisin kuin lista, monikko on kuitenkin muuttumaton: siihen ei voi lisätä
# alkioita eikä siitä voi poistaa alkioita monikon luonnin jälkeen.

lista[0] = 0
lista.append(7)
print("muokattu lista", lista, "ensimmäinen muutettu nollaksi ja viimeiseksi lisätty 7")


# Monikkoa on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jono on
# luonteeltaan staattinen: tiedetään, että muutoksille ei ole tarvetta ohjelman suorituksen aikana.
# tämä ei toimi monikolla, on muokkaamaton
# monikko[0] = 0

luku = monikko[4]
print("hain tämän monikosta: ", luku)

#tämä oli vain esimerkistä
'''
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
'''

# Monikon läpikäynti samalla tavalla kuin listan.

sanat = ("eka", "toka", "kolmas", "neljäs", "viides")
for sana in sanat:
    print(sana)
    if sana == "neljäs":
        print ("sana neljäs löytyi!!!")

if "viides" in sanat:
    print("sana viides löytyi!!!!!!!!!11")

# Monikon arvojen purku muuttujiin

hedelmät = ("Mansikka", "Banaani", "Ananas")
print(hedelmät)
(eka, toka, kolmas) = hedelmät
print ("Monikko purettu muuttujiin, tässä eka", eka)

# Monikon voi antaa funktiolle parametrina

def tulosta_monikko(hedelmät):
    for h in hedelmät:
        print(h)

tulosta_monikko(hedelmät)

# Monikko funktionpaluuarvona
# Yksinkertaistetaan random

def heitä1():
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    #print(f"nopista tuli silmäluvut {noppa1}, {noppa2}")

    noppa1, noppa2 = random.randint(1, 6), random.randint(1, 6)
    print(f"nopista heitä1 tuli silmäluvut {noppa1, noppa2}")
heitä1()


def heitä2():
    noppa1, noppa2 = random.randint(1, 6), random.randint(1, 6)
    print(f"nopista heitä2 tuli silmäluvut {noppa1, noppa2}")
heitä2()


def heitä3():
    noppa1, noppa2 = random.randint(1, 6), random.randint(1, 6)
    print(f"nopista tuli silmäluvut {noppa1, noppa2}")
heitä3()

#noppa1, noppa2 = heitä3()
#print("funktiosta heitä3 palautu arvot:", noppa1, noppa2)

print("--------------------------")

# Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.
# Koska joukon alkioille ei ole määritelty järjestystä, ei alkioihin voi myöskään viitata indeksillä.
# Toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen,
# eli joukossa ei voi olla kahta samansisältöistä alkiota.

joukko = {1, 2, 3, 4, 5, 6}
print(joukko)

numeroiden_lista = [1, 2, 3, 4, 5, 6, 6]
numeroiden_monikko = (1, 2, 3, 4, 5, 6, 6)
print(f"numero 6 EI voi esiintyä joukossa useasti")
numeroiden_joukko = {1, 2, 3, 4, 5, 6,6}
print(numeroiden_joukko)

numeroiden_joukko.add(6)
numeroiden_joukko.add(7)
print(numeroiden_joukko)
numeroiden_joukko.remove(1)
print(numeroiden_joukko)

pelit = {"Monopoli", "Shakki", "Cluedo", "Muuttuva labyrintti", "Kimble"}
print(pelit)
pelit.remove("Monopoli")
print(pelit)


# alkioiden iteroiminen läpi for/in rakentellaa
# indeksiin ei voi tosiaan tässä viitata
for p in pelit:
    print(p)

if "Kimble" in pelit:
    print (f"Kimble löytyi 😊👌")

print("-----------------------")



autolista = []
autolista.append('Lexus')
print(autolista)
print(type(autolista))


# tyhjä joukko luodaan listaan verrattuna eri tavalla, set-funktion avulla

autojoukko = set()
autojoukko.add("Audi")
print(autojoukko)
print(type(autojoukko))

# jos yrität luoda tyhjää joukkoa {}- aaltosulkeilla, tästä tulee sen jälkeen sanakirja
# tässä ihmetellään mikä on sanakirja

print("SANAKIRJA\n")

# Sanakirja (dictionary on Pythonin käytetyimpiä tietorakenteita.
# sanakirjaan voidaan tallentaa avain-arvopareja.


# kun sanakirja alustetaan, annetaan avain-arvopari seuraavasti AVAIN : ARVO
# peräkkäiset avain-arvoparit erotellaan pilkuilla

oppilaat = {"Amber": 43,
            "Bonny": 23,
            "Clint": 57,
            "Daniel": 34,
            "Eemeli": 20
}
print(oppilaat)

# mitä ovat tietueet (items) sanakirjassa
print(oppilaat.items())

# mitä ovat avaimet sanakirjassa
print(oppilaat.keys())

# mitä ovat arvot / values sanakirjassa
print(oppilaat.values())

# käydään läpi sanakirja nyt for / in rakenteilla
# kierrosmuuttuja eli tässä tapauksessa o saa arvokseen
# kukin sanakirjassa esiintyvän AVAIMEN
for o in oppilaat:
    print(o)

avain = "Amber"
oppilaat[avain]
print("Etsitään avaimella AMBER hänen ikä", oppilaat["Amber"])
print(f"Danielin ikä {oppilaat["Daniel"]}")

for o in oppilaat:
    print(f"oppilaan nimi {o} ikä on {oppilaat[o]} ")

# hae haluttu ikä if / in rakennetta käyttäen
# 1. pyydä käyttäjältä nimi ja haetaan se sanakirjasta


nimi = input("anna nimi jota etsit sanakirjasta: ")
if nimi in oppilaat:
    ikä = oppilaat[nimi] # haetaan avaimella arvo
    print (f"oppilaan nimi löytyi"
           f"hänen ikä on {ikä}")
else:
    print(f"Nimeä {nimi} ei löytynyt")


yhteystiedot = {
    "Amber": {
        "puh": "045642263",
        "osoite": "Kauratie 4"
    },
    "Bonny": {
        "puh": "0464358437",
        "osoite": "Luksuskuja 9"
    },
    "Clint": {
        "puh": "05043285439",
        "osoite": "Kattopolku 52"
    },
}
print(f"Amberin puhelinnumero {yhteystiedot["Amber"]["puh"]}")

oppilaat2 = {"Amber": 43,
            "Bonny": 23,
            "Clint": 57,
            "Daniel": 34,
            "Eemeli": 20,
            "Emma" : [1, 2, 3, 4]
}

# lisätään uusi oppilas
# llisätään avaimen avulla, mikäli avain jo löytyy niin tämä päivittää tiedot

oppilaat2 ["Juuso"] = 22
oppilaat2["Amber"] = [22, 53, "muutin tämän"]
oppilaat2["Amber"] = "Morooo"
oppilaat2["Amber"] = 66
print(oppilaat2)

# muokkaa jos on olemassa, muuten lisää
oppilaat2.update({"Timo": 88, "Laura": 75, "Daniel": 33})
print(oppilaat2)


