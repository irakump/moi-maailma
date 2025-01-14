# Tehtävä 8.3
# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa
# lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie
# asennus loppuun.

import mysql.connector

connection = mysql.connector.connect(
             host='127.0.0.1',
             port= 3306,
             database='flight_game',
             user='ira',
             password='lunni',
             autocommit=True
             )

from geopy import distance

def count_distance(icao1, icao2):                       #funktio
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = 'EFHK';"
    sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = 'EFIV';"
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.execute(sql2)
    result = cursor.fetchall()
    #geopystä joku kutsu tähän  ? ? ?
    result1 = (distance.distance(paikka1, paikka2).km)
    print(result)
    print(f"Lentokenttien välinen etäisyys on {result} kilometriä.")
    return

first_icao = "EFHK"     #Helsinki
second_icao = "EFIV"    #Ivalo

count_distance(first_icao, second_icao)

#int(distance) = #tähän joku syöte       #distance = etäisyys

# print(f"Lentokenttien välinen etäisyys on {etaisyys} kilometriä.



# first_icao = input("Kerro lentokentän ICAO-koodi: ")
# second_icao = input("Kerro toisen lentokentän ICAO-koodi: ")

