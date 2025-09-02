# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

app_running = True
pienin_numero = None
suurin_numero = None

while app_running:
    luku = input("Kirjoita luku: ")

    if luku == "": # jos laittaa tyhjän merkkijonon looppi loppuu
        print("lopetetaan...")
        app_running = False
    else:
        luku_int = int(luku) # muuttaa luvun integeriksi
        if pienin_numero is None or luku_int<pienin_numero:
            pienin_numero = luku_int
        if suurin_numero is None or luku_int>suurin_numero:
            suurin_numero = luku_int

#tulostaa pienimmän ja suurimman luvun, jotka kirjotettiin
print("pienin numero: ", pienin_numero)
print("suurin numero: ", suurin_numero)

