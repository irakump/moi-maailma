# Tehtävä 8.3
# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa
# lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie
# asennus loppuun.

import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
             host='127.0.0.1',
             port= 3306,
             database='flight_game',
             user='ira',
             password='lunni',
             autocommit=True
             )

def find_coordinates(icao_code):                                #funktio
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{user_input}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#pääohjelma
user_input = input("Kerro lentokentän ICAO-koodi: ")            #kysytään ICAO-koodi
airport1 = (find_coordinates(user_input))                       #tallennetaan koordinaatit muuttujaan

user_input = input("Kerro toisen lentokentän ICAO-koodi: ")     #kysytään toinen ICAO-koodi
airport2 = (find_coordinates(user_input))                       #tallennetaan

distance = (distance.distance(airport1, airport2).km)           #geopyn avulla lasketaan etäisyys (km)
print(f"Lentokenttien etäisyys on {distance:.1f} kilometriä.")
