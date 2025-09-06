# Tehtävä 2, kysyy laivan hyttiluokan (LUX, A, B, C), sen jälkeen tulostaa sen sanallisen kuvauksen.


laivan_hytti = input("Kirjoita tähän haluamasi laivan hytti (LUX, A, B, C): ") # kysyy minkä hytin haluaa valita
LUX = "LUX"
A = "A"
B = "B"
C = "C"


# tulostaa laivan_hytti -muuttujaan kirjoitetun vastauksen mukaisen tiedotteen
if laivan_hytti == LUX:
    print("LUX on parvekkeellinen hytti yläkannella.")
elif laivan_hytti == A:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif laivan_hytti == B:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif laivan_hytti == C:
    print("C on ikkunaton hytti autokannen alapuolella.")