# valintarakenne-esimerkkejä (mod03)
import random

# onko_totta = False
# onko_totta = 3 == 3

satunnaisluku = random.randint(0, 100)

#print(f"Arvottu luku: {satunnaisluku}") tätä voi käyttää debuggaamiseen, eli virheiden selvittämiseen

# kolikonheittosimulaattori
if satunnaisluku < 50:
    print("Kruuna")
    print("Kuuluu samaan koodilohkoon")
elif satunnaisluku > 50:
    print("Klaava")
else: # toteutuu muissa tapauksissa, eli jo arvottu luku on tasan 50 (tod.näk: 1/100
    print("Kolikko jäi pystyyn!!!")


print("Ohjelman suoritus if-lauseen jälkeen jatkuu tästä.")

# dummy-kirjautuminen
oikea_salasana = "salamana"
tunnus = "nuutti"
input_tunnus = input("Käyttäjätunnus: ")
input_salasana = input("Kirjoita minulle salasanasi: ")

if input_salasana == oikea_salasana and input_tunnus == tunnus:
    print ("Tervetuloa!")
    kehote = input("Oikea salasana. Mitäs sä haluut tehä??")
    if kehote == "moikata":
        print("No moro!! :D")
    else:
        print("en ymmärtänyt kehotetta")
else:
    print("Väärä salasana!!!!!")
print("Ohjelma suljettu... . .  .   .    .    .    .")

