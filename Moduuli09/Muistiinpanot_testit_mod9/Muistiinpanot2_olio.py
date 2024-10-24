# OLIO - Tuntimuistiinpanot
from cgitb import small

# ennen oliota ominaisuuksien tallentamisen keinoja: lista (kun ei vielä tiedä olioista)

# luodaan lista, jonka sisällä on sanakirjoja (yksi koira yhdessä sanakirjassa)
koirat = [
    {"koira": "Lissu", "vuosi": 2015},
    {"koira": "Reko", "vuosi": 2016}
]
"""
print(koirat)
eka_koira = koirat[0]
print(eka_koira["koira"])

for k in koirat:
    print(k)  # tulostuu koirakohtainen sanakirja
"""

###############################

# OLIO - tapa 1 = "tyhmä tapa"

# Luokka on "ohje" olion luomiselle

# luodaan luokka, käytä isoja kirjaimia. Esim. Koira, KoiraHoitola, KissaKahvila
class Koira:
    pass

# Olio on luokan ilmentymä
# Pääohjelmasta voi luoda useita olioita

# Luodaan koira-oliot
ullan_koira = Koira()
esterin_koira = Koira()

# Annetaan koira-olioille ominaisuuksia
# ominaisuudet ovat oliokohtaisia; kaikki ovat koiria, mutta nimi, syntymävuosi, rotu tms. muuttuu
ullan_koira.nimi = "Lissu"
ullan_koira.syntymavuosi = 2015

esterin_koira.nimi = "Reko"
esterin_koira.syntymavuosi = 2016

#############
print()
#############

print(f"Ullan koiran nimi on {ullan_koira.nimi} ja syntymävuosi on {ullan_koira.syntymavuosi}.")
print(f"Esterin koiran nimi on {esterin_koira.nimi} ja syntymävuosi on {esterin_koira.syntymavuosi}.")

# Yllä (Olio 1) tehtiin luokka ilman ominaisuuksia ja metodeja, ominaisuudet annettiin yksi kerrallaan = työlästä
# Oikea / parempi tapa on määritellä ja alustaa ominaisuudet luokan avulla (Olio tapa 2)

# OLIO - TAPA 2 = parempi tapa

#############
print()
#############

# Luokkien perusrakenne - luokkien nimissä on CamelCase

# __init__ on (erityinen) funktio, jota kutsutaan konstruktoriksi
# tätä funktiota kutsutaan aina automaattisesti, kun luodaan luokasta olio / instanssi
# alustajan (eli konstruktion) loppuun EI kirjoiteta return-lausetta!

# luodaan luokka
class LuokanNimi:
    def __init__(self, parametri1, parametri2):
        self.attribuutti = parametri1                    # nimetään parametrit
        self.attribuutti = parametri2

    # metodi
    def metodi1(self):
        return
    def metodi2(self):
        return

# esim. luodaan koira-luokka siten, että se alustaa koirien ominaisuudet
class Dog:
    def __init__(self, name, year, owner, size, colour):
        self.name = name
        self.year = year
        self.owner = owner
        self.size = size
        self.colour = colour

    def print_information(self):
        print(f"Nimi on {self.name}, syntymävuosi on {self.year} ja omistaja on {self.owner}.")

# luodaan pääohjelma, joka kutsuu koira-luokkaa

dog1 = Dog("Lissu", 2015, "Ulla", "pieni", "harmaa")
dog2 = Dog("Reko", 2016, "Esteri", "iso", "ruskea")
dog3 = Dog("Musti", 2023, "Hermeli", "normaali", "musta")

print(f"Ensimmäisen koiran nimi on {dog1.name}, syntymävuosi {dog1.year} ja omistaja on {dog1.owner}.")
print(f"Toisen koiran nimi on {dog2.name}, syntymävuosi {dog2.year} ja omistaja on {dog2.owner}.")
print(f"Kolmannen koiran nimi on {dog3.name}, väri {dog3.colour} ja koko {dog3.size}.")

#######
print()
#######

# METODI
# laajennetaan yllä olevaa ohjelmaa ja tehdään sinne metodi, jossa printataan koirien tiedot

# kutsutaan funktiota
dog1.print_information()
dog2.print_information()
dog3.print_information()

# voisi tehdä myös erilaisia metodeja, jos haluaa vaikka palauttaa vain värin tai koiran nimen ja omistajan.

#######
print()
#######

# esimerkkiohjelma - lisätään konstruktori (voi lisätä valmiiksi oletusarvon)

class Kissa:
    def __init__(self, nimi, syntymavuosi, maukuminen="meow"):  # oletusarvo maukumiselle määritelty
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.maukuminen = maukuminen

    def puhu(self, kerrat):
        print(f"Kissa {self.nimi} maukuu {kerrat} kertaa: ")
        for i in range(kerrat):
            print(self.maukuminen)
        return

# pääohjelma
# luodaan kissat, määritellään ominaisuudet
kissa1 = Kissa("Mouru", 2022)   # ei määritellä maukumista, joten tulee oletusarvo
kissa2 = Kissa("Catcat", 2018, "meeeooowwwww")
kissa3 = Kissa("Pörrö", 2020, "miu-miu")
kissa4 = Kissa("Mörkö", 2019)

# kutsutaan konstruktoria?

kissa1.puhu(5)
kissa2.puhu(3)
kissa3.puhu(2)

#######
print()
#######

# LUOKKAMUUTTUJA (staattinen muuttuja)
# ominaisuudet ovat oliokohtaisia, esim. kaikilla luokan olioilla on oma nimi
# luokkamuuttujaan voi tallentaa kaikille olioille yhteistä tietoa, esim. kuinka monta oliota on luotu,
#    esim. koirien lukumäärä (eli kuinka monta koira-luokan ilmentymää on luotu)
# luokkamuuttuja sijoitetaan alustajan (__init__) ulkopuolelle eli ennen sitä

# esim. luokkamuuttuja

class Kissa:

    tehdyt_kissat = 0       # luokkamuuttuja, jonka määrää kasvatetaan aina kun luodaan uusi kissa

    def __init__(self, nimi, syntymavuosi, maukuminen="meow"):      # oletusarvo maukumiselle määritelty
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.maukuminen = maukuminen
        Kissa.tehdyt_kissat = Kissa.tehdyt_kissat + 1

    def puhu(self, kerrat):
        print(f"Kissa {self.nimi} maukuu {kerrat} kertaa: ")
        for i in range(kerrat):
            print(self.maukuminen)
        return

kissa1 = Kissa("Mouru", 2022)   # ei määritellä maukumista (attribuuttia), joten tulee oletusarvo
kissa2 = Kissa("Catcat", 2018, "meeeooowwwww")
kissa3 = Kissa("Pörrö", 2020, "miu-miu")
kissa4 = Kissa("Mörkö", 2019)

print(f"Luodaan uusia kissoja: {kissa1.nimi}, {kissa3.nimi}, {kissa4.nimi} ja {kissa2.nimi}.")
print(f"Kissoja on nyt {Kissa.tehdyt_kissat}.")

#######
print()
#######

# Lisää esimerkkejä luokista, tuntiesimerkit

    # def on konstruktori (metodi)

# voi määritellä valmiiksi auton ominaisuuksia, jotka tulevat luodessa
class Auto1:
    def __init__(self):
        self.rekisteritunnus = "ABC-123"
        self.huippunopeus = 100

auto1 = Auto1()
print(f"Auton {auto1.rekisteritunnus} huippunopeus on {auto1.huippunopeus} km/h.")

# voi määritellä parametrit, jotka käyttäjän pitää itse määritellä oliota luodessa
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.nopeus = 0             # tämä on kovakoodattu, eli nopeutta ei voi itse määrittää alussa
        self.huippunopeus = huippunopeus

    def tulosta_ominaisuudet(self):
        print(f"Rekkari: {self.rekisteritunnus}, huippunopeus: {self.huippunopeus} km/h, "
              f"tämänhetkinen nopeus: {self.nopeus} km/h.")

    def kiihdyta(self):
        self.nopeus = self.nopeus + 10      # tai self.nopeus += 1

auto2 = Auto("ABC-987", 120)
auto3 = Auto("EDF-456", 150)

auto2.tulosta_ominaisuudet()
auto3.tulosta_ominaisuudet()

# parametreja voi myös määritellä jälkikäteen
#auto2.rekisteritunnus = "ERT-789"
#auto2.tulosta_ominaisuudet()

# samaan olioon voi viitata useasta muuttujasta, esim. auto2 = auto3, jolloin auto2 ja auto3 viittaavat
# molemmat olioon, joka on tallennettu muuttujaan auto3 (eli auto3 yhteydessä olevaan olioon)

# nyt kiihdyta-konstruktorissa nopeus lisääntyy 10 km/h, eli voi kiihdyttää useaan kertaan:

auto2.kiihdyta()
auto2.kiihdyta()
auto2.kiihdyta()

auto2.tulosta_ominaisuudet()

