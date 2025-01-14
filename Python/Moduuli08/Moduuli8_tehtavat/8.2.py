# Tehtävä 8.2
# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa
# olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
            host='127.0.0.1',
            port= 3306,
            database='flight_game',
            user='ira',
            password='lunni',
            autocommit=True,
            charset = 'utf8mb4',
            collation = 'utf8mb4_general_ci'
             )

def list_airports_per_types(iso_country):                               #funktio
    sql = (f"SELECT type, count(*) FROM airport "
           f"WHERE iso_country = '{user_input}' GROUP BY type;")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(f"Lentokentän tyyppi: {row[0]}, lukumäärä: {row[1]}")     #tulostetaan yksitellen tyyppi ja lkm

#pääohjelma
user_input = input("Syötä maakoodi: ")
list_airports_per_types(user_input)                 #kutsutaan muuttujaa käyttäjän syöttämällä maakoodilla
