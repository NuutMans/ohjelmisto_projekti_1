nimi = "Maukku"
nimi2 = "Jorkku"
num1 = 42
num2 = 143

print(f"Hei {nimi}, ikäsi on {num2}")

# tyhjä lista
tyhja = []

# lista voi sisältää muuttujia, nemoroita, merkkijonoja, jne.
nimet = ["Jorma", "Loru", 82, nimi, nimi2, "Dani", "Sami", "Harri"] # tässä listassa on alkioita
print (nimet)

# lista voi sisältää myös toisia listoja
ikalista = [74, 45, 93, [94, 36]]
print(ikalista)

# printtaa listan pituuden
print(len(nimet))

lempinumerot = [147, 314, 527]
lempinimet = ["Ronnie", "Barry", "Judd", "Si Jiahui", "Allen"]
# nämä nimet listassa on alkioita, alkio on listan jäsen / tieto


# listasta voidaan hakea tietoa alkion indeksin avulla
# TAI viipaloimalla
# alkioon viitataan indexinumerolla, alkaen numerosta 0, eli 0 on ns. ensimmäinen(1st)
print(f"Moikka {lempinimet[0]} ja terve myös {lempinimet[3]}")

print(ikalista[3][1])
print(len(ikalista))

print("---------------------------")

nimet2 = ["Lino", "Liano", "Elias", "Malia", "Alina", "Emma", "Maela", "Liam"]
print(nimet2[5]) # Emma
print(nimet2[3]) # Malia
print(nimet2[1:5]) # Liano - Alina (EI printtaa Emmaa)
print(nimet2[:4])
print(nimet2[:-4])
print(nimet2[1:-1])
print(nimet2[1:-1:2])
print("--------------------------------------")



# uusi_lista = vanha_lista[alku:oppu:askel]
uusi_lista = nimet2 [2:4]
print(nimet2)
print(uusi_lista)

#lista jossa on 5 kaupunkia
#tulosta 3 ensimmäistä
print("----------------------")
kaupungit = ["helsinki", "oslo", "kuopio", "turku", "kalajoki"]
print(kaupungit[:3])
print(kaupungit[-1])

# viittaus listan ulkopuolelle aiheuttaa virheen!!
# print(kaupungit[8])

print("HARJOTE ----------------------------------- HARJOTE")

kaupungit.append("!tokio!")
print(kaupungit)
# kaupungit.remove("rovaniemi") -> virhe, koska kaupunkia ei löydy

if "helsinki" in kaupungit:
    print(f"!!!!helsinki lyötyi ja postetaan listasta!!!!!!!!!!!!")
    #poistetaan helsinki
    kaupungit.remove("helsinki")
    print(kaupungit)

#lisätään tampere ensimmäiseksi
kaupungit.insert(0, "helsinki")
print(kaupungit)

#tutkitaan monesko indeksi
monesko = kaupungit.index("turku")
print("monesko turku on?:", "no se on", monesko)


#lisätään muita kaupunkeja listaan kaupungit
lisaa_kaupunkeja = ["sodankylä", "öulu", "lappeenranta"]
kaupungit.extend(lisaa_kaupunkeja)
print(kaupungit)

# muokataan olemassa oleva alkiota indeksin avulla

kaupungit[-2] = "oulu"
print(kaupungit)

print("-------------------------")

hedelmia = ["appelsiini", "greippi", "Apprikoosi", "omena", "Omena"]
numerolista = [40, 288, 49, 7203, 42, 63, 85]

hedelmia.sort() # täytyy sortata / järjestää ennen kuin voi printata
print(hedelmia) # printattu sorttaamisen jälkeen
print(numerolista)

numerolista.sort(reverse=True)
print("tässä on numerolista järjestettynä suurimmasta pienimpään", numerolista)

tottavaiei = True # python on dynaamisesti tyypitetty, eli boolean
tottavaiei = "True" # nyt string
print(type(tottavaiei))

viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko"]

print(viikonpaivat)

print("-------------------")
print("Muutamia hyödyllisiä funktioita tulevaisuutta varten")
print("-------------------")

# len, sum, min , max count
luvut = [2, 4, 6, 7, 8, 2, 2, 2, 7]

print(len(luvut)) # listan pituus
print(sum(luvut)) # lukujen summa
print(min(luvut)) # pienin numero
print(max(luvut)) # isoin numero
print(luvut.count(2)) # kuinka monta kakkosta on listassa


print("-------------------")
print("Muutamia hyödyllisiä funktioita tulevaisuutta varten")
print("-------------------")

# käydään luvut läpi iteroimalla

# luvut = [2, 4, 6, 7, 8, 2, 2, 2, 7]
i = 0
while i < len(luvut):
    # print(i)
    print(luvut[i])
    i += 1

print("-------------------")

for lukuja in luvut:
    print(luvut)
print("kysy ullalta tästä printistä ^")

print("-------------------")

# tässä kirjain on kierrosmuuttuja
for kirjain in "abcdefghijk":
    print(kirjain)

print("-------------------")

# tässä tapauksessa alkio on kierrosmuuttuja
for alkio in [1, 2, 3, 4, 5, 6,]:
    print(alkio)

print("--------------------")

# tässä kaupunki on kierrosmuuttuja
for kaupunki in kaupungit:
    print(kaupunki)

print("------------------")

for numero in range(30):
    print(numero)

for n in range(4, 80):
    print(n)

print("--------------------")
print("nurinpäin")
for n in range(100, 0, -4): #vitosesta nollaan (eli ykköseen) asti asekeleet(-4)
    print(n)

print("tässä loppu")

luvut_listan_pituus = len(luvut)
for n in range(luvut_listan_pituus):
    # print(n) - tämä on iteraattori
    print(luvut[n])

print("--------------------")

# printataan vain 3
for n in range(3):
    print(kaupungit[n])
