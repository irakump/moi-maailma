# Tuntiesimerkkejä, SQL-tehtäviin ohjeita/vinkkejä.
#
# Mod8.1 tehtävään vinkkejä:

# mysql:ssä: describe airport;

# select ident, name, municipality from airport;        #näitä tarvitaan jossakin tehtävässä?
# rivi 5: noin 71 000 riviä

#kannattaa tehdä tehtävä niin, että itse koodissa ei tarvitse käydä kaikkia rivejä läpi, vaan se
#tehdään jo SQL-kyselyssä

#select ident, name, municipality from airport where ident = "ZYTH";
#yllä oleva korjattuna (ident ei tarvitse): select name, municipality from airport where ident = "ZYTH";

#############

#tehtävä 8.1:

import mysql.connector

connection = mysql.connector.connect(
             host='127.0.0.1',
             port= 3306,
             database='flight_game',
             user='ira',
             password='lunni',
             autocommit=True
             )

def fetch_airport_by_icao(code):                            #funktio hakee sql:stä dataa
    sql = (f"SELECT name, municipality "
           f"FROM airport WHERE ident = '{code}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    return result_row               #palauttaa monikon, paitsi jos tyhjä tulosjoukko --> None

user_input = input("Anna ICAO-koodi: ")
airport = (fetch_airport_by_icao(user_input))

if airport != None:
    print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}")        #hakee 0. ja 1. alkiot
else:
    print("Lentokenttää ei löydetty annetulla koodilla.")

#pitkät sql-lauseet voi pilkkoa pienemmiksi laittamalla eri riveille (kuten yllä), liian pitkät on vaikea
#lukea

# ctrl + z -toiminnolla saa takaisin edellisen jutun, jos vaikka vahingossa poistaa koodia :-)

#kovakoodaa ensin tehtävään joku vastaus, ennen kuin kysytään tieto käyttäjältä --> helpompi testata.
#esim. rivi 39 voisi tehtävää tehdessä olla: airport = (fetch_airport_by_icao("ZYTH"))

#SQL: tietojen/arvojen lisäys tauluun:
# INSERT INTO airport (id, ident) VALUES (999, 'joku_nimi_tahan');
# INSERT INTO airport (id, ident, name, municipality) VALUES (999, 'joku_nimi_tahan2', 'oma kentta', 'Espoo');


# EXTRA: Tiedon lisäys tietokantaan - jos tämän pyörittää, tieto lisätään lentopeli-tietokantaan !! (älä sotke)
"""
def add_airport(ICAO, name, municipality):
    sql = (f"INSERT INTO airport (id, ident, name, municipality)"
           f"VALUES (999, '{ICAO}', '{name}', '{municipality}');")          #id 999 on vain joku esimerkki
    cursor = connection.cursor()
    cursor.execute(sql)

new_icao = input("Anna uusi ICAO: ")
new_name = input("Anna uuden kentän nimi: ")
new_municipality = input("Anna paikkakunta: ")
add_airport(icao, name, municipality)
"""

# Tiedon poistaminen tietokannasta: tulee ajaa koko tietokanta source-komennolla
# script on tavallaan varmuuskopio, eli jos muokkaa tietokantaa vaikka tehtävää tehdessä, voi sen vain
# ajaa uudelleen.

# voi myös poistaa yksittäisen:
# delete from airport where ident = "tähän haluttu ident, esim. 999"
# jos ajaa komennon: delete from airport    - poistuu koko airport-taulu.

#mod 8, teht. 8.2
#enemmänkin harjoitusta sql:n käyttöön

#SQL:
# describe airport                         -hakee kaikki "otsikot" taulusta
# show tables                              -näyttää kaikki tietokannan taulut
# select type from airport group by type;  -saa kaikki airport-taulun tyypit, tulostuu vain yksi (ei duplikaatteja)

