# Tehtävä 8.1
# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia
# vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

connection = mysql.connector.connect(                                            #SQL-yhteys
             host='127.0.0.1',
             port= 3306,
             database='flight_game',
             user='ira',
             password='lunni',
             autocommit=True
             )

def find_airport_information(icao_code):                                         #luodaan fuktio
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"Lentokentän nimi on {result[0][0]} ja sijaintikunta {result[0][1]}.")
    return

#pääohjelma
icao_code = input("Kerro lentoaseman ICAO-koodi: ")                     #kysytään syöte käyttäjältä
find_airport_information(icao_code)                                     #kutsutaan muuttujaa
