# osio 2.




import math


nimi = input("Anna nimesi: ")
tervehdys = "Moi " + nimi + "!"

#tervehtii nimen syötän jälkeen
print(tervehdys)

ympyran_sade = float(input("Anna ympyrälle säde: ")) # esim 8
pinta_ala = math.pi * (ympyran_sade ** 2)

print(f"Tässä on ympyrän pinta-ala: {pinta_ala}")
print("Hyvää työtä!!!")

# ympyrän ala: pi * r^2: 3.14159 * r^2
# piin arvo
# print(math.pi * r^2)


# tehtävä 3
# suorakulmion piiri = kaikki sivut summattuna yhteen
# suorakulmion pinta-ala = kanta * korkeus

suorakulmion_korkeus = float(input("anna suorakulmiolle korkeus: "))
print(suorakulmion_korkeus)
suorakulmion_leveys = float(input("Anna suorakulmiolle leveys: "))

suorakulmion_piiri = suorakulmion_leveys + suorakulmion_korkeus + suorakulmion_leveys + suorakulmion_korkeus

print(f"Tässä on suorakulmion piiri: {suorakulmion_piiri}")




