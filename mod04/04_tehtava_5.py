# mod04 tehtävä 5
'''

Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen (python) ja salasanan (rules)
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty

'''




oikea_salasana = "rules"
oikea_tunnus = "python"
yritykset = 5


while yritykset > 0:

    input_tunnus = input("Käyttäjätunnus: ")
    input_salasana = input("Kirjoita minulle salasanasi: ")
    yritykset -= 1

    if input_salasana == oikea_salasana and input_tunnus == oikea_tunnus and yritykset > 0:
        print ("Tervetuloa!")
        break

    elif input_salasana != oikea_salasana or input_tunnus != oikea_tunnus and yritykset > 0:
            print(f"Väärä salasana! Yrityksiä jäljellä: {yritykset}")

    elif yritykset <= 0:
        print("Salasana meni liian monta kertaa väärin. Ohjelma päättyy...")
        break
