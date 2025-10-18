'''Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma
tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta
nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.'''


kaupungit = []


for k in range(5):
    kaupungin_nimi = input("anna kaupungin nimi: ")
    kaupungit.append(kaupungin_nimi)

print("annoit kaupungit: ")
for kaupungin_nimi in kaupungit:
    print(kaupungin_nimi)