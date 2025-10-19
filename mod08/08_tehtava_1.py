import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1", # oletusarvo, ei ole pakollinen parametri
    port=3306, # oletusarvo, ei ole pakollinen parametri
    database="flight_game",
    user="python1",
    password="TietokantaPython1",
    autocommit=True
)


def get_airport_icao_code(icao_code):

    sql = f"SELECT name, municipality, ident FROM airport WHERE ident = %s; "
    cursor = connection.cursor()
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()
    if result:
        
        print(f"{icao_code} - {result[0]}, {result[1]}")
    else:
        print("lentokenttää ei löytynyt")

icao_input = input("Anna lentokentän ICAO-koodi: ")
get_airport_icao_code(icao_input)