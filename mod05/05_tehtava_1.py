'''
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran
kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-looppia
'''

import random


lukumäärä = int(input("anna arpakuutioiden lukumäärä: "))
heitot = []

for n in range(lukumäärä):
    silmäluku = random.randint(1,6)
    heitot.append(silmäluku)
    print(silmäluku)

summa = sum(heitot)
print (f"Silmälukujen summa {summa}")