import random
from tabulate import tabulate

# Tehtävä 10.4
# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina
# kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan
# nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
# *tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# *tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# *kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
# kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle
# annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä
# kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
# onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta_tilanne-metodin avulla kymmenen tunnin välein sekä
# kertaalleen sen jälkeen, kun kilpailu on päättynyt.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus    # kilpailun pituus kilometreinä
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            arvottu_nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(arvottu_nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        autot2 = []

        for auto in autot:
            auto2 = [auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka]
            autot2.append(auto2)
        taulukko = tabulate(autot2, headers=["Rekisteritunnus", "Huippunopeus (km/h)", "Nopeus (km/h)", "Kuljettu matka (km)"],
                            tablefmt="pretty")
        print(taulukko)

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.kuljettu_matka >= self.pituus:
                print(f"Kilpailu päättyy - auto {auto.rekisteritunnus} voittaa!")
                return True
        return False

# pääohjelma

# luodaan 10 autoa, tallennetaan listaan
autot = []
for i in range(1, 11):
    arvottu_huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i}", arvottu_huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
print(f"Kilpailu alkaa! Voittaja on se, joka kulkee ensimmäisenä {kilpailu.pituus} km.")
kilpailu_paattyy = False
tunnit = 0

while not kilpailu_paattyy:     # ohjelma pyörii, kunnes kilpaily_paattyy on True
    kilpailu.tunti_kuluu()
    kilpailu_paattyy = kilpailu.kilpailu_ohi()
    tunnit += 1
    if tunnit % 10 == 0 and kilpailu_paattyy:
        break
    elif tunnit % 10 == 0:
        print(f"Kilpailu on kestänyt {tunnit} tuntia. Tilanne on seuraava: ")
        kilpailu.tulosta_tilanne()

print(f"Kilpailun kesto: {tunnit} tuntia. Tulokset:")
kilpailu.tulosta_tilanne()
