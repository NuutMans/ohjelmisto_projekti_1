# while-toistolause eli silmukka eli luuppi
import random

suorita_silmukka = True

while suorita_silmukka: # tekee yhden loopin, koska alempana on ensimmäisenä suorita_silmukka = False
    suorita_silmukka = False
    print("totta") # \n tarkoittaa new line
    print("on") # \t tarkoittaa (tab) tabulaattori
print("silmukan suoritus loppui")


# iteraattori ja while, iteraattori tarkoittaa kasvavaa tai pienenevää arvoa
# arvo on kovakoodattu "hard coded", voi kysyä myös käyttäjältä: toistojen_lkm = int(input("Montako kertaa tervehditään: "))
toistojen_lkm = 1000
i = 0

while i < toistojen_lkm: #niin kauan kuin iteraattorin arvo on pienempi kuin 0, toistetaan tätä
    print(f"iteroiva silmukka, i:n arvo: {i}")
    i = i + 3
    # lyhyt tapa: i += 1

print(f"i:n arvo lopuksi: {i}")


# komentorivisovellus / komentokehotesovellus
app_running = True # muuttujan nimi kertoo miten sovellus toimii, helpottaa lukemista kun kuvaa dataa mikä siellä on sisällä
# "main loop"
while app_running:
    command = input("Komento> ")
    print(f"Komentosi oli: {command}")
    if command == "lopeta":
        app_running = False
    elif command == "laskukone":
        luku1 = float(input("anna ensimmäinen luku: "))  # esim. "10" -> 10.0
        luku2 = float(input("anna toka luku: "))  # esim. "20" -> 20.0
        tulos_yhteenlasku = luku1 + luku2
        print("Yhteenlaskutoimituksen tulos: " + str(tulos_yhteenlasku))




# print(f"Arvottu luku: {satunnaisluku}") # tätä voi käyttää debuggaamiseen, eli virheiden selvittämiseen

# kolikonheittosimulaattori n ketroo kuinka monta kertaa kolikko jäi pystyyn

n = 10000
i = 0
kolikko_pystyssa_lkm = 0
while i < n:
    i += 1
    satunnaisluku = random.randint(0, 1000)
    print(f"Arvottu luku: {satunnaisluku}")
    if satunnaisluku < 500:
        print("Kruuna")
    elif satunnaisluku > 500:
        print("Klaava")
    else: # toteutuu muissa tapauksissa, eli jo arvottu luku on tasan 50 (tod.näk: 1/100
        print("Kolikko jäi pystyyn!!!")
        kolikko_pystyssa_lkm += 1
print(f"Kolikko jäpi pystyyn {kolikko_pystyssa_lkm} kertaa.")


# muokattu noppaesimerkki materiaalista 03
#noppa1 = 0
#noppa2 = 0
#heitot = 0
pelikerrat = 0
heittojen_kokonaislkm = 0

app_running = True
while app_running:
    noppa1 = noppa2 = heitot = 0 #ketjutettu muuttujat, sama kuin kirjoittaisi muuttujat erikseen kuten yläpuolella
    while noppa1 != 6 or noppa2 != 6: # jos jompikumpi arvo on alle 6
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    print(f"Kahteen kutoseen tarvittiin {heitot:d} heittoa.")
    pelikerrat = pelikerrat + 1
    heittojen_kokonaislkm = heittojen_kokonaislkm + heitot
    komento = input("Pelataanko uudestaan (k/e)?")

print(f"Kaksi kutosta saatiin keskimäärin {heittojen_kokonaislkm/pelikerrat}")