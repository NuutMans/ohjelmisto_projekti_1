# mod02 tehtävät




import math
import random

nimi = input("Anna nimesi: ")
tervehdys = "Moi " + nimi + "!"

#tervehtii nimen syötän jälkeen
print(tervehdys)

ympyran_sade = float(input("Anna ympyrälle säde: ")) # esim 8
pinta_ala = math.pi * (ympyran_sade ** 2)

print(f"Tässä on ympyrän pinta-ala: {pinta_ala:.5f}")
print("Hyvää työtä!!!")

# ympyrän ala: pi * r^2: 3.14159 * r^2
# piin arvo
# print(math.pi * r^2)


# tehtävä 3
# suorakulmion piiri = kaikki sivut summattuna yhteen
# suorakulmion pinta-ala = kanta * korkeus

suorakulmion_korkeus = float(input("anna suorakulmiolle korkeus: "))

suorakulmion_leveys = float(input("Anna suorakulmiolle leveys: "))

suorakulmion_piiri = suorakulmion_leveys + suorakulmion_korkeus + suorakulmion_leveys + suorakulmion_korkeus

print(f"Tässä on suorakulmion piiri: {suorakulmion_piiri}")

suorakulmion_pinta_ala = suorakulmion_leveys * suorakulmion_korkeus
print(f"Tässä on suorakulmion pinta-ala: {suorakulmion_pinta_ala}")

# tehtävä 4
# kysyy 3 kokonaislukua, kertoo tulon, keskiarvon ja summan

luku1 = float(input("Kirjoita ensimmäinen kokonaisluku: "))
luku2 = float(input("Kirjoita toka luku: "))
luku3 = float(input("Kirjoita kolmas luku: "))

summa = luku1 + luku2 + luku3
keskiarvo = summa / 3
tulo = luku1 * luku2 * luku3

print (f"Tässä on lukujen tulo: {tulo}")
print (f"Tässä on lukujen keskiarvo: {keskiarvo:.3f}")
print (f"Tässä on lukujen summa: {summa}")



# Tehtävä 5
# ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.


'''    
    Yksi leiviskä on 20 naulaa. = yksi leiviskä on 8512 g   | 8 kilogrammaa ja 512 grammaa
    Yksi naula on 32 luotia. = yksi naula on  g   | 0 kilogrammaa ja 425,6 grammaa
    
    Yksi luoti on 13,3 grammaa.   | 0 kilogrammaa ja 13,3 grammaa
    1kg on 1000 grammaa
'''

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

leiviska_g = leiviska * 8512
naula_g = naula * 425.6
luoti_g = luoti * 13.3

kokonaispaino = leiviska_g + naula_g + luoti_g

kilogrammat = kokonaispaino // 1000
grammat =  kokonaispaino - 1000 * kilogrammat

print("Massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat:.3f} grammaa.")


'''
Kirjoita ohjelma, joka 

    arpoo ja tulostaa kaksi erilaista numerolukon koodia:

    kolmenumeroisen koodin, arpoo numeromerkki on väliltä 0..9

    nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

print

koodi_1: 123

koodi_2: 2341

'''

kolme_yksi = random.randint(0, 9)
kolme_kaksi = random.randint(0, 9)
kolme_kolme = random.randint(0, 9)

nelja_yksi = random.randint(1, 6)
nelja_kaksi = random.randint(1, 6)
nelja_kolme = random.randint(1, 6)
nelja_nelja = random.randint(1, 6)

koodi_1 = kolme_yksi, kolme_kaksi, kolme_kolme
koodi_2 = nelja_yksi, nelja_kaksi, nelja_kolme, nelja_nelja

print (f"koodi 1 :{koodi_1}")
print (f"koodi 2 :{koodi_2}")