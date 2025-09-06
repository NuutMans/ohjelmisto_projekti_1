# mod04 tehtävä 5

oikea_salasana = "rules"
oikea_tunnus = "python"
yritykset = 5

# kirjautumislooppi, joka kysyy kirjautumista 5 kertaa, jonka jälkeen lopettaa ohjelman, jos kirjautumiset on väärin
while yritykset > -1:

    input_tunnus = input("Käyttäjätunnus: ")
    input_salasana = input("Salasana: ")
    yritykset -= 1


    if input_salasana == oikea_salasana and input_tunnus == oikea_tunnus and yritykset > -1:
        print ("Tervetuloa!")
        break
    elif input_salasana != oikea_salasana or input_tunnus != oikea_tunnus and yritykset > -1:
        print(f"Väärä salasana! Yrityksiä jäljellä: {yritykset}")

    elif yritykset <= 0:
        print("Salasana meni liian monta kertaa väärin. Ohjelma päättyy...")

        break
