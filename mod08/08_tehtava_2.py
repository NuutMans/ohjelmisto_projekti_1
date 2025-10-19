import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1", # oletusarvo, ei ole pakollinen parametri
    port=3306, # oletusarvo, ei ole pakollinen parametri
    database="flight_game",
    user="python1",
    password="TietokantaPython1",
    autocommit=True
)

def get_airports_with_country_code(country_code):
    cursor = connection.cursor()
    sql = "SELECT type, count(*) FROM airport WHERE iso_country = %s GROUP BY type;"
    cursor.execute(sql, (country_code,))
    results = cursor.fetchall()

    if results:
        print(f"Lentokenttätyypit maassa {country_code}: ")
        for type, count in results:
            print(f"{type}: {count} kpl")
    else:
        print("Lentokenttiä ei löytynyt annetulla maakoodilla.")


user_input = input("Anna maakoodi (esim. FI): ").strip().upper()
get_airports_with_country_code(user_input)