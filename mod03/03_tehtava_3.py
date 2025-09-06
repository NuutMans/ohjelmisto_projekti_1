
# Tehtävä 3, Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

sukupuoli = input("Kirjoita sukupuoli (nainen tai mies): ") # kysytään sukupuolen muuttuja

hemoglobiini = float(input("Kirjoita hemoglobiiniarvo: ")) # kysytään hemoglobiinin arvo

if sukupuoli == "nainen" and hemoglobiini >= 117 and hemoglobiini <= 175:
    print("Hemoglobiiniarvosi on normaali") # jos sukupuoli on nainen ja hemoglobiinin arvo on 117 ja 175 välillä, tulostaa normaali
elif sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiiniarvosi on alhainen") # jos sukupuoli on nainen ja hemoglobiinin arvo on alle 117, tulostaa alhainen
elif sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiiniarvosi on korkea") # jos sukupuoli on nainen ja hemoglobiinin arvo on yli 175, tulostaa korkea

if sukupuoli == "mies" and hemoglobiini >= 134 and hemoglobiini <= 195:
    print("Hemoglobiiniarvosi on normaali")  # jos sukupuoli on mies ja hemoglobiinin arvo on 134 ja 195 välillä, tulostaa normaali
elif sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiiniarvosi on alhainen") # jos sukupuoli on mies ja hemoglobiinin arvo on alle 134, tulostaa alhainen
elif sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiiniarvosi on korkea") # jos sukupuoli on mies ja hemoglobiinin arvo on yli 195, tulostaa korkea
