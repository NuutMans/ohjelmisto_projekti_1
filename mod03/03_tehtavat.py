# mod03 tehtävät

# tehtävä 1, kuhan pituus, päästä vapaaksi jos liian pieni

kuhan_pituus = float(input("Hei kalastaja! Kerro minulle senttimetreissä kuinka iso kuha on: "))
print(f"Kuhasi on {kuhan_pituus} cm pitkä")

# kysyy kuhan pituutta
if kuhan_pituus >= 42:
    print("Laita kuha koriin. Kuha on yli 42cm pitkä! Sinun ei tarvitse päästää sitä vapaaksi!")

# jos kuhan pituus on alle 42cm, ohjelma kehottaa päästää sen vapaaksi.
if kuhan_pituus < 42:
    print("Päästä kuha vapaaksi. Se on liian pieni. Kuhan täytyy olla yli 42cm, jotta voit pitää sen!!!")
    print(f"Kuhasi täytyy olla {42 - kuhan_pituus:.2f} cm pidempi")
# kuhan lakisääteinen alamitta on 42 senttimetriä

# Tehtävä 2, kysyy laivan hyttiluokan (LUX, A, B, C), sen jälkeen tulostaa sen sanallisen kuvauksen.


laivan_hytti = input("Kirjoita tähän haluamasi laivan hytti (LUX, A, B, C): ")
LUX = "LUX"
A = "A"
B = "B"
C = "C"

if laivan_hytti == LUX:
    print("LUX on parvekkeellinen hytti yläkannella.")
elif laivan_hytti == A:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif laivan_hytti == B:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif laivan_hytti == C:
    print("C on ikkunaton hytti autokannen alapuolella.")

# toimii

# Tehtävä 3, Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

sukupuoli = input("Kirjoita sukupuoli (nainen tai mies): ")

hemoglobiini = float(input("Kirjoita hemoglobiiniarvo: "))

if sukupuoli == "nainen" and hemoglobiini >= 117 and hemoglobiini <= 175:
    print("Hemoglobiiniarvosi on normaali")
elif sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiiniarvosi on alhainen")
elif sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiiniarvosi on korkea")

if sukupuoli == "mies" and hemoglobiini >= 134 and hemoglobiini <= 195:
    print("Hemoglobiiniarvosi on normaali")
elif sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiiniarvosi on alhainen")
elif sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiiniarvosi on korkea")
