#Tenttikertaus, mod8
#RELAATIOTIETOKANNAN KÄYTTÖ
#testiesimerkki: haetaan Ankkalinna-tietokannasta käyttäjän syöttämän lemmikin omistaja (nimi)

import mysql.connector

connection = mysql.connector.connect(
             host='127.0.0.1',
             port= 3306,
             database='ankkalinna',         #tähän tietokannan nimi
             user='ira',
             password='lunni',
             autocommit=True
             )

def find_pet_owner(pet_name):
    sql = (f"SELECT etunimi, sukunimi FROM ankkalinnalainen "
           f"INNER JOIN omistaa ON ankkalinnalainen.id = ankkalinnalainen_id "
           f"INNER JOIN lemmikki ON lemmikki.id = lemmikki_id "
           f"WHERE lemmikki.nimi = '{user_input}';")
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #print(result)          #tässä tulostuu listana: esim. [('Mikki', 'Hiiri')]
    return result

user_input = input("Kerro lemmikin nimi, niin etsin sen omistajan: ")
owner_name = find_pet_owner(user_input)           #haetaan lista, mutta ei tulosteta sitä, tallennetaan
print(f"Lemmikin {user_input} omistaja on {owner_name[0][0]} {owner_name[0][1]}.")

#lemmikin omistajan nimi tallentuu listana muuttujaan owner_name. Eli owner_name on lista, jonka..
#.. alkiot ovat monikoita! Siksi pitää hakea listan alkiosta 0 edelleen 0. monikon alkio, ja
#seuraavassa haetaan edelleen listan alkiosta 0 monikon alkio 1.
