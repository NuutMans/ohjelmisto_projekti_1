import mysql.connector

# otetaan tietokantaan yhteys

connection = mysql.connector.connect(
    host="127.0.0.1", # oletusarvo, ei ole pakollinen parametri
    port=3306, # oletusarvo, ei ole pakollinen parametri
    database="flight_game",
    user="python1",
    password="TietokantaPython1",
    autocommit=True
)

#print(connection)
# luodaan osoitin ja sijoitetaan viittaus siihen muuttujaan
cursor = connection.cursor() # cursorilla ajetaan komentoja. Vähän kuin kirjottaisi MySql MariaDB -clienttiin
# käytetään osoitinta tietokantahakuun
cursor.execute("SELECT name, iso_country FROM country") # ei tarvitse puolipistettä Python-koodissa
result = cursor.fetchone() # palauttaa rivin pyydety sarakkeen monikkon
print(result)
result = cursor.fetchone() # palauttaa yhden rivin monikkona
print(result)
result = cursor.fetchmany(3) # hakee niin monta kun laittaa sulkuihin. Palauttaa "rivimonikot" eli monta riviä listana [], joka sisältää monikkoja.
print(result)
#yleisin tapa: haetaan kaikki loput tulokset
result = cursor.fetchall()
print(result)
print(f"Result: {len(result[0][1])}")

# tulostetaan ensimmäisen rivin maakoodi
print(result[0])

# tulostetaan tulosjoukko muotoiltuna
for country in result:
    print(f"Maan {country[0]} maakoodi on: {country[1]}")

# funktio, joka hakeen maan sen koodin perusteella

def get_country_name_by_code(code):
    sql = f"SELECT name FROM country WHERE iso_country = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    # jos tulosjoukko on tyhjä, eli maakoodilla ei löydy maata
    #if not result: #result == None: molemmat palauttaa Maakoodi: (käyttäjän virheellinen input), hakutulos: Ei löydy. Voi tehdä kahdella tavalla
    if result:
        return  result[0]
    return "ei löydy" # jos ei laita [0] funktiosta tulostuu ('Taiwan',)
#    return f"maan {code} nimi: {result}"

# "käyttöliittymä maanhakusovellukseen"

country_code = input("anna maakoodi: ") # input tallennetaan muuttujaan
country = get_country_name_by_code(country_code)
print(f"Maakoodi: {country_code}, hakutulos: {country}")

# SQL insert esimerkki, uuden maan lisäys country-tauluun.
def add_country(code, name): # suluissa oleva on parametri
    sql = f"INSERT INTO country (iso_country, name) VALUES ('{code}', '{name}')'"
    cursor = connection.cursor()
    # HUOM: kaattu usql-virheeseen, jos yritetään syöttää samaa pääavainarvoa uudelleen
    #Virhekäsittely käsitellään myöhemmin...
    cursor.execute(sql)
    #print(curosr)
#add_country("xyz", "testcountry")

