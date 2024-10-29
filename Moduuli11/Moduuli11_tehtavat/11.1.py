# Tehtävä 11.1
# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
# alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
# julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
# julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

# yliluokka
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")

# aliluokka
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}")

# aliluokka
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")

# pääohjelma
lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()
print()
kirja.tulosta_tiedot()
