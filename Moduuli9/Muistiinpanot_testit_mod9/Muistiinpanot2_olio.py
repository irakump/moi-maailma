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
