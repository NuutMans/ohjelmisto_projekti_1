# 20.8. tunti

"""
monirivinen kommentti (merkkijono, string)
voidaan myös sijoittaa muuuttujaan
"""

import math
import random

nimi = input("Anna nimesi: ") # palauttaa merkkijonoon (str)
ika = 30 # kokonaisluku (int)
ika_ensi_vuonna = ika + 1 # int
str_ika_ensi_vuonna = str(ika_ensi_vuonna) # -> "31"




tervehdys = "moi " + nimi + " " + str_ika_ensi_vuonna


print("tänään oli kaunis aamu!")


print(tervehdys)

# simppeli laskukone

# luetaan käyttäjältä kaksi luku (str), jotka muunnetaan samantien
# liukuluvuksi ja sijoitetaan muttujiin
luku1 = float(input("anna ensimmäinen luku: ")) # esim. "10" -> 10.0
luku2 = float(input("anna toka luku: ")) # esim. "20" -> 20.0

# lasketaan tulos numeraalisilla arvoilla
# tulos = int(luku1) + int(luku2) # kokonaisluvuilla
tulos_yhteenlasku = luku1 + luku2 # liukuluvuilla
tulos_vahennyslasku = luku1 - luku2
tulos_jakolasku = luku1 / luku2
kokonaisosa = luku1 // luku2
jakojaannos = luku1 % luku2
tulos_kertolasku = luku1 * luku2
tulos_potenssiin_korotus = luku1 ** luku2


# tulos = 1+2 # 3 (kovakoodattu arvo test)
print("yhteenlaskutoimituksen tulos: " + str(tulos_yhteenlasku))
print("vähennyslasku tulos: " + str(tulos_vahennyslasku))
print(f"jakolaskun tulos: {luku1 / luku2:.2f}, jossa kokonaisosa on "
      f"{kokonaisosa}, desimaaliosa {tulos_jakolasku - kokonaisosa:.2f} ja "
      f"jakojaannos {jakojaannos}")
print("kertolaskun tulos: " + str(tulos_kertolasku))

# tulosta loput tulokset

print(f"pii: {math.pi:.8f}")
# satunnaisluvun generointi
print(random.randint(1, 6))
