# dummy-kirjautuminen
'''

Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen (python) ja salasanan (rules)
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty

'''




oikea_salasana = "rules"
oikea_tunnus = "python"
input_tunnus = input("Käyttäjätunnus: ")
input_salasana = input("Kirjoita minulle salasanasi: ")
app_running = True
login_tries = 5

#voi tehdä while komennolla loopin, jossa kysyy salasanaa ja tunnusta vaikka 3 kertaa. Jos ne on 3 kertaa väärin heittää käyttäjän ulos
while app_running and login_tries > 0:

    if input_salasana == oikea_salasana and input_tunnus == oikea_tunnus:
        print ("Tervetuloa!")
        login_tries -= 1
        app_running = False
    else:
        if app_running == False or login_tries > 0:
            login_tries -= 1
            print("Väärä salasana! Yritä uudelleen. Yrityksiä jäljellä:", login_tries)

# koodi toimii tällä hetkellä niin, että looppi menee yksi kerrallaan lopuun asti 4, 3, 2, 1 yritystä jäljellä.
# mutta ei kysy uudelleen tunnusta tai salasanaa
# todo: mitesn saan koodin niin (loopille?) että jokaisella kerralla kysyy salasanaa uudelleen?

#if login_tries == 0:
#login_tries -= 1

