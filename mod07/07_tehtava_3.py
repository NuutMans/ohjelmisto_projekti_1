# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä
# syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta
# kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)




#lentoasema_ohjelma = True

#while lentoasema_ohjelma:
#    lentoasema = input("Kirjoita ICAO-koodi: ")

icao_list = {
    "EFHN": "Hangon lentoasema",
    "EFHK": "Helsinki-Vantaa lentoasema",
    "EFTP": "Tampere-Pirkkalan lentoasema",
    "MSSM": "El Papalon lentoasema",
    "CYSW": "Sparwood lentoasema"

}


ask = True

while ask:

    cmd = input("haluatko syöttää uuden lentoaseman u(), hakea jo syötetyn lentoaseman (h) vai lopettaa(l): ").lower()

    if cmd == "u":
        print("lisätään uusi kenttä")
        icao = input("anna ICAO-koodi: ").upper()
        name = input("annd lentokentän nimi: ")
        icao_list[icao] = name
        print("lentokenttä lisätty: ", icao_list)
    elif cmd == "h":
        print("haetaan lentokenttä")
        icao = input("anna ICAO-koodi mitä haetaan (EFHN): ").upper()
        if icao in icao_list:
            print(f"haulla {icao} löytyi lentokenttä: {icao_list[icao]}")
    elif cmd == "l":
        print(f"❌Lopetetaan")
        ask = False
    else:
        print(f"💀 virheellinen syöte, ohjelma lopetetaa...")
        ask = False




