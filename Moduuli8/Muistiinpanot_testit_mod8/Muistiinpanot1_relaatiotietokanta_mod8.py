# RELAATIOTIETOKANNAN KÄYTTÖ (MODUULI 8, VKO 4)

# SQL-connector-python 8.0.29 asennettu. Pitää asentaa jokaiseen projektiin erikseen, nyt asennettu
# moi-maailma -projektiin.
# tietokantaa voi käyttää seuraavilla komennolla:
import mysql.connector

connection = mysql.connector.connect(        #tällä yhdistää lentopeli-tietokantaan
             host='127.0.0.1',      #tietokoneen IP-osoite eli localhost (ei tarvitse muuttaa, viittaa omaan koneeseen)
             port= 3306,            # "netin kautta" yhteys tietokantaan, ei tarvitse nyt muuttaa
             database='flight_game',    #tietokannan nimi
             user='ira',            #oma käyttäjänimi
             password='lunni',      #oma salasana (ei kannata käyttää henkilökohtaista salasanaa, koska näkyy koodissa)
             autocommit=True
             )

#connect() on valmis funktio, joka palauttaa tietokantayhteyden, ja tämä pitää sijoittaa muuttujaan!
#yllä muuttuja on connection.

#jos asentaa SQL-connector-python 9.0.0 -version, tulee tehdä *joku juttu*, että lentopeli-tietokantaan
#saa yhteyden:
# import mysql.connector        #tämän lisäksi pitääkö tehdä jotakin??
# collation = ' (tähän ks. koodi malliesimerkeistä '    #collation siis autokommit=True -kohdan alle.

# print(connection)   #testi, tätä ei tarvitse oikeasti, tuloste:
# <mysql.connector.connection_cext.CMySQLConnection object at 0x000002322DC06C40>

############
#nämä kaikki pitää tehdä (ainakin cursor tulee yhdistää):

cursor = connection.cursor()     #luodaan osoitin (=cursor) tietokantaan, tallennetaan muuttujaan

#ajetaan sql-kielinen kysely osoittimen avulla:

sql = ("SELECT continent, name, iso_country FROM country")
cursor.execute(sql)
#sql: laita merkkijonona, select ja from ei ole pakko olla isolla, mutta se on SQL:ssä yleinen tapa,
# eli kannattaa kirjoittaa. Joissakin "oikeissa" ympäristöissä niillä voi olla merkitystä, eli
# edelleen kannattaa kirjoittaa isolla.

"""
result = cursor.fetchone()
print(result)                   #tässä tulee ensimmäinen rivi (tietue??)
result = cursor.fetchone()
print(result)                   #tässä tulostuu toinen rivi, kursori siirtyy yhden askeleen seuraavaan

#fetchmany() -komento palauttaa halutun määrän rivejä kerrallaan --> sulkuihin
#fetchmany palauttaa aina LISTAN, esim. fetchmany(3) palauttaa seuraavat kolme monikkoa listan muodossa,
#.. jatkaa aina siitä, mihin kursori on jäänyt

result = cursor.fetchmany()     #oletusarvo on 1, eli sama kuin: result = cursor.fetchmany(1)
print(result)

result = cursor.fetchmany(3)
print(result)

#fetchall() palauttaa kaikki (loput) rivit listana.
result = cursor.fetchall()
print(result)
"""

#tuloslista käsitellään toistorakenteella:

#haetaan ensin kaikki ("SELECT name, iso_country, continent FROM country")
result = cursor.fetchall()      #nimi voisi olla myös results tai rows
print(result)

for row in result:      #muuttujan nimi tässä on row
    print(row)

#indeksit numeroimalla voi viitata eri järjestyksessä ylhäällä olevaan sql-muuttujaan
for row in result:
    print(f"Rivi: {row[1]}, maakoodi: {row[2]}, maanosa: {row[0]}")
if cursor.rowcount > 0:
    print(f"Tulosrivejä käyty läpi (kursorin sijainti): {cursor.rowcount}")
else:
    print("Ei tuloksia.")

#####
print()
#####

#cursor.rowcount    laskee sql-taulussa olevat rivit, jotka kursori on KÄYNYT LÄPI.
# eli kertoo kursorin sijainnin (tässä kursori on käynyt läpi KAIKKI tulokset):
print(f"Rivejä käyty läpi yhteensä: {cursor.rowcount}")        #tulostaa: ... 248

#esim. jos hakee 3 riviä ihan alussa, ennen muuta koodia (pitää tehdä kuitenki sql-komento)
result = cursor.fetchmany(3)
print(result)
print(f"Rivejä käyty läpi yhteensä: {cursor.rowcount}")     #tuloksen pitäisi olla 3 ?


#SQL-kyselyiden tulosteet ovat MONIKKO


