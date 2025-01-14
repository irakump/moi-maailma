#Moduuli 9
#olio-ohjelmointi - luokka, olio, alustaja

#luokka:
#Olio-ohjelmoinnissa luokalla tarkoitetaan yleiskäsitettä, joka määrittää yleiset ja
#yhteiset piirteet, joita sen jäsenillä on.

#esim. luokka: koira
#pienin mahdollinen luokkarakenne:


class Koira:         #class-komennolla tehdään luokka, tässä sen nimi on koira
    pass            #pass on tyhjä lause, joka ei tee mitään.

#luokan määrityksen rungossa on oltava ainakin yksi lause (esim. pass)

#luodaan luokasta olio: koira-olio, jonka syntymävuosi on 2022 ja nimi Rekku
koira = Koira()         #tämä lause luo Koira-olion, johon viitataan muuttujalla koira.
koira.nimi = "Rekku"    #asetetaan nimi
koira.syntymavuosi = 2022       #asetetaan syntymävuosi

print(f"{koira.nimi} on syntynyt vuonna {koira.syntymavuosi}.")

#ominaisuudet ovat oliokohtaisia, eli ominaisuuksiksi voi asettaa mitä tahansa ja ne voivat poiketa toisistaan
#esim. kaikilla koirilla olisi nimi ja syntymävuosi, mutta joillakin myös rotu ja/tai lempinimi.

#Huomaa Python-kielen vakiintunut kirjoitustapa luokkien nimille: ne kirjoitetaan isoin alkukirjaimin.
#Jos luokan nimi koostuu useammasta sanasta, sanat kirjoitetaan yhteen ilman alaviivamerkkiä siten, että
#kukin sana aloitetaan isolla alkukirjaimella. Tästä kirjoitustyylistä käytetään nimitystä CamelCase.
# Esimerkki tällaisesta luokan nimestä on NäytönSuorakulmio.

#Alustaja eli konstruktori:
#Olioiden luonnin helpottamiseksi luokan sisälle kirjoitetaan usein alustaja eli konstruktori,
# joka automaattisesti asettaa halutut arvot luotavan olion ominaisuuksiksi.

class Koira2:
    def __init__(self, nimi, syntymavuosi):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi

koira2 = Koira2("Rekkis", 2021)
print(f"{koira2.nimi} on syntynyt vuonna {koira2.syntymavuosi}.")

#Python-kielen alustaja määritetään luokan sisällä kirjoittamalla funktio, jonka nimenä on __init__
#Funktion ensimmäiseksi parametriksi määritetään aina self. Tämän jälkeen määritellään muut parametrit,
#jotka alustajalle halutaan antaa.
#Alustajan loppuun ei kirjoiteta return-lausetta (kuten muilla funktioilla).
#Uuden olion ominaisuuksiin viitataan kirjoittamalla varattu sana self, minkä jälkeen tulee piste
# ja halutun ominaisuuden nimi.
#Uuden olion ominaisuuden arvoksi annetaan tyypillisesti alustajan parametrina saatu arvo. Esimerkiksi lause
# self.nimi = nimi antaa uuden olion nimi-ominaisuuden arvoksi nimi-parametrimuuttujan arvon.

#Huomaa, että oliota luotaessa alustajan ensimmäinen parametri self ohitetaan kokonaan. Ei siis kirjoiteta:
#VÄÄRIN: koira = Koira(self, "Rekku", 2022)

#OIKEIN: koira = Koira("Rekku", 2022)

#METODIT:
#oliolle voi määrittää toimintoja, joita kutsutaan metodeiksi (metodi on funktio)
#kirjoitetaan koira-luokkaan hauku-metodi, jota voidaan kutsua:

class Koira:
    def __init__(self, nimi, syntymavuosi, haukahdus = "Vuh vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range (kerrat):
            print(self.haukahdus)
        return

koira1 = Koira("Muro", 2019)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

koira1.hauku(2)
koira2.hauku(5)

# Alustajan parametreja on nyt kolme. Viimeiselle parametrille (haukahdus) on annettu oletusarvo,
# joka asetetaan silloin, kun parametria ei oliota luetaessa anneta. Esimerkissä Muro-koira saa siis
# oletushaukahduksen.
# Metodin ensimmäiseksi parametriksi asetetaan aina self

# Metodin sisällä voidaan viitata olion omiin ominaisuuksiin siten, että kirjoitetaan self, jota seuraa piste
# ja ominaisuuden nimi. Esimerkiksi ilmaisu self.haukahdus viittaa kulloisenkin olion
# haukahdus-ominaisuuden arvoon.

#Luokkamuuttuja eli staattinen muuttuja:
#Toisinaan on tarve tallentaa jokin koko luokkaa koskeva tieto, joka ei liity mihinkään yksittäiseen
# luokan olioon. Esimerkiksi Koira-luokan tapauksessa tällainen ominaisuus voisi olla tieto siitä, montako
# koiraa (eli Koira-luokan ilmentymää) kaiken kaikkiaan on luotu. Tällainen tieto voidaan tallentaa
# luokkamuuttujaan eli staattiseen muuttujaan.

class Koira:

    tehty = 0                   #luokkamuuttuja sijoitetaan alustajan (def __init__) ulkopuolelle!

    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")
print (f"Koiria on nyt {Koira.tehty}.")
#yllä tulostuu "Koiria on nyt 2", koska on luotu kaksi koiraa.

