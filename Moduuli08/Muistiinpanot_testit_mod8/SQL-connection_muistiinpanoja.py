# SQL-ohjeita ja esimerkkejä kursorista (cursor), fetchall() -komento yms.

# SQL-connection tulee lisätä koodiin, jotta SQL-komentoja voi antaa PyCharmin kautta

# ladattu uusin sql-connection -versio, eli aina kun ottaa yhteyden sql niin pitää lisätä
# ylimääräinen rivi "collation" connection-muuttujaan!
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='treasure_chest',
    user='treasure',
    password='chest',
    autocommit=True,
    collation='utf8mb4_general_ci'
)

#jos on vanhempi versio, yhteys otetaan näin
import mysql.connector

connection = mysql.connector.connect(
             host='127.0.0.1',
             port= 3306,
             database='flight_game',
             user='ira',
             password='lunni',
             autocommit=True
             )
#Luodaan ensin muuttuja:
def do_something():
    #tulee myös määrittää kursori (cursor):
    cursor = connection.cursor()
    # Tämän jälkeen kursoria pyydetään suorittamaan merkkijonomuuttujassa oleva SQL-lause:
    # ennen tätä pitää siis määritellä sql-komento, esim sql = f"SELECT lemmikki, omistaa from ankkalinna"
    cursor.execute(sql)
    #Sen jälkeen tulosjoukko on pyydetään palvelimelta:
    result = cursor.fetchall()
    return

#fetchall() hakee tulosjoukon kokonaisuudessaan. Jos on tarvetta rajata (harvoin), voi käyttää:
#fetcone() -hakee yhden tuloksen, tai fetchmany(), johon voi määrittää, kuinka monta tulosta hakee. esim (5).

#result-muuttujaan tallennettu tulosjoukko on rakenteeltaan lista, jonka alkiot ovat monikoita. !!!!

# Ulomman rakenteen (listan) kukin alkio vastaa yhtä tulosjoukon riviä.
# Jokainen rivi esitetään monikkona (muuttumaton), ja sen alkioina ovat kenttien arvot siinä järjestyksessä
# kuin ne SELECT-lauseessa määriteltiin.

#malliesimerkki materiaalista - funktioon tulee määrittää sql-kysely ja kursorin asiat:
import mysql.connector

def hae_työntekijät_sukunimellä(sukunimi):
    sql = f"SELECT Numero, Sukunimi, Etunimi, Palkka FROM Työntekijä where Sukunimi='{sukunimi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return

# Pääohjelma
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ihmiset',
         user='dbuser',
         password='sAL_a3ana',
         autocommit=True
         )

sukunimi = input("Anna sukunimi: ")
hae_työntekijät_sukunimellä(sukunimi)

######################

# Yhteys muodostetaan tietokanta-ajurin connect-metodin avulla.
# Katsotaan metodin parametreja tarkemmin:

# host määrittää tietokoneen, johon yhteys otetaan. Kun yhteys otetaan samassa koneessa olevaan palvelimeen, jossa Python-ohjelmaa ajetaan, kirjoitetaan osoitteeksi 127.0.0.1 tai vaihtoehtoisesti localhost.
# port määrittää tietoliikenneportin, jota tietokantapalvelin kuuntelee. MariaDB:n käyttämä portti on 3306, jos et ole erikseen muuttanut sitä.
# database määrittää tietokannan nimen.
# user määrittää käyttäjätunnuksen, jolla tietokantaa käytetään. Python-sovellusta varten kannattaa luoda oma käyttäjätunnus, jolla on tarvittavat oikeudet datan lukemiseen ja muokkaamiseen. Muita oikeuksia tuolle käyttäjätunnukselle ei yleensä tule antaa.
# password määrittää käyttäjätunnukseen liittyvän salasanan. Huomaa, että Internetin kautta käytettäviä Python-ohjelmia ajetaan taustapalvelimella, jolloin loppukäyttäjällä ei ole pääsyä salasanan sisältävään Python-koodiin.
# autocommit kertoo, sitoutetaanko jokainen SQL-operaatio välittömästi omana transaktionaan. Tähän kannattaa normaalisti asettaa arvoksi True, jolloin yksittäisten päivityslauseiden (esim. UPDATE) sitouttamisesta COMMIT-lausein ei tarvitse erikseen huolehtia.
