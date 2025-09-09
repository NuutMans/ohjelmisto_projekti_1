# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

# joukkotietorakenne = set
# järjestys on aina muuttuva, ei voida käyttää indeksiä
# voidaan lisätä ja poistaa eli voi muokata


# nimilista = {"Moona", "Kari"}



nimijoukko = set()

kysy = True
# lisää nimi listaan
while kysy:
    nimi = input("syötä uusi nimi nimilistaan: ").lower().strip()

    if nimi == "":
        kysy = False
        print("Ohjelma loppuu...")
    #tutki onko nimi jo listassa
    elif nimi in nimijoukko:
        print(f"{nimi} löytyy jo listasta. Aiemmin syötetty nimi.")

    else:
        nimijoukko.add(nimi)
        print(f"Uusi nimi. {nimi} lisätty listaan")

print("Kaikki syötetyty nimet 💖:")
for nimi in nimijoukko:
    print(nimi)


#nimilista = set()

#while True:
#   nimi = (input("syötä uusi nimi nimilistaan: "))

#    if nimi == "": break

