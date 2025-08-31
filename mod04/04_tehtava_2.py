# mod 4 tehtävä 2

# TODO: kirjoita ohjelma, joka printtaa tuloksen, kunnes käyttäjä kirjoittaa negatiivisen luvun
# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

# tee looppi joka printtaa niin kauan kunnes laittaa negatiivisen määrän tuumia

app_running = True


while app_running: # looppi joka kysyy kuinka monta tuumaa haluat muuttaa senttimetreiksi
    tuumat = float(input("kuinka monta tuumaa haluat muuttaa senttimetreiksi?: ")) # kysyy tuumien määrän käyttäjältä
    senttimetri = tuumat * 2.54 # tuumien muutos senttimetreiksi
    print(f"{tuumat} tuumaa on {senttimetri} senttimetriä") # tulostaa tuumien määrän senttimetreissä
    if tuumat <= 0: # jos tuumat on alle 0 tai negatiivinen
        app_running = False # lopettaa loopin