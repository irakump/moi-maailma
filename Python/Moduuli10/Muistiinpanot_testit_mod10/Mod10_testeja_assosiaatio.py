# testejä, malliesimerkit

# ohjelmassa on ilmentymiä (=olioita) kahdesta eri luokasta
# Hoitola- ja Koira-luokkien välillä on pysyvä assosiaatiosuhde:
    # Hoitola-oliolla on instanssimuuttuja, joka sisältää viittaukset Koira-olioihin
    # assosiaatiosuhde on tässä yksisuuntainen - Hoitola-olio tietää, mitä koiria kulloinkin on hoitossa
    # koira-olio ei tiedä mitään hoitolasta, jossa se (mahdollisesti) on

# assosiaatiosuhteen voi toteuttaa yksi- tai kaksisuuntaisena (kaksisuuntaista kannattaa käyttää vain silloin, kun
# sille on hyvät perusteet (ei tarvitse turhaan huolehtia, että eri suuntiin olevien olioviittausten pitää olla sisällöiltään
# synkronoidut)

# PYSYVÄ ASSOSIAATIOSUHDE (Hoitola tuntee Koira-luokan)

# luodaan koira-luokka
class Koira:
    def __init__(self, nimi, vuosi, haukahdus="vuh vuh"):   # nämä ovat parametreja
        self.nimi = nimi
        self.vuosi = vuosi
        self.haukahdus = haukahdus

    # metodi
    def hauku(self, kerrat):
        for i in range(kerrat):
            print(f"{self.nimi} haukkuu: {self.haukahdus}")
        return

# luodaan koirahoitola-luokka
class Hoitola:
    def __init__(self):
        self.koirat = []

    # metodi
    def koira_sisaan(self, koira):
        self.koirat.append(koira)
        print(f"{koira.nimi} kirjattu sisään")
        return

    # toinen metodi
    def koira_ulos(self, koira):        # tässä parametrina on koira
        self.koirat.remove(koira)
        print(f"{koira.nimi} kirjattu ulos")

    # kolmas metodi
    def tervehdi_koiria(self):          # tässä ei ole parametreja
        for koira in self.koirat:
            print(f"Hei, {koira.nimi}!")
            koira.hauku(1)

# pääohjelma
koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "wooffff")

hoitola = Hoitola()

hoitola.koira_sisaan(koira1)
hoitola.koira_sisaan(koira2)
hoitola.tervehdi_koiria()

hoitola.koira_ulos(koira2)
hoitola.tervehdi_koiria()

##
print()
##

# TILAPÄINEN ASSOSIAATIOSUHDE (esimerkki - auton ja maalaamon välinen suhde)

class Auto:
    def __init__(self, rekisteritunnus, vari):
        self.rekisteritunnus = rekisteritunnus
        self.vari = vari

class Maalaamo:
    def maalaa(self, auto, vari):
        auto.vari = vari

maalaamo = Maalaamo()
auto = Auto("ABC-123", "sininen")
print("Auto on " + auto.vari)
maalaamo.maalaa(auto, "punainen")
print("Auto on nyt " + auto.vari)

# yllä olevassa esimerkissä maalaamo tuntee maalattavan auton vain maalaa-etodin suorituksen ajan, sillä viittaus Auto-olioon
# on saatu metodikutsun parametrina
# Kun metodin suoritus päättyy, parametrimuuttujaan (auto) ei enää pääse käsiksi
# Myöskään auto ei tiedä maalaamosta mitään (auton tietoja ei ole tallennettu maalaamoon esim. listaan, eikä maalaamon
# tietoja ole tallennettu Auto-luokkaan
