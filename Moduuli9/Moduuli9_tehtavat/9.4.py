import random
from tabulate import tabulate

# Tehtävä 9.4
# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1",
# "ABC-2" jne.
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

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

# pääohjelma
autot = []      # tyhjä lista

# luodaan 10 autoa
for i in range(1, 11):
    arvottu_huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i}", arvottu_huippunopeus)     # luodaan auto
    autot.append(auto)                                            # lisätään listaan

print("Kilpailu alkaa! Voittaja on se, joka kulkee ensimmäisenä 10 000 km.\n...")

tunnit = 1
kilpailu_ohi = False

while not kilpailu_ohi:     # ohjelma pyörii, kunnes kilpailu_ohi on True
    for auto in autot:
        arvottu_nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(arvottu_nopeuden_muutos)
        auto.kulje(1)  # auto kulkee tunnin ajan muuttuneella nopeudella
        if auto.kuljettu_matka >= 10000:
            print(f"Kilpailu päättyy - auto {auto.rekisteritunnus} voittaa! Kilpailu kesti {tunnit} tuntia.")
            kilpailu_ohi = True
            break
    tunnit += 1

# muutetaan oliot lista-muotoon
autot2 = []

for auto in autot:
    auto2 = [auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka]
    autot2.append(auto2)

taulukko = tabulate(autot2, headers=["Rekisteritunnus", "Huippunopeus (km/h)", "Nopeus (km/h)", "Kuljettu matka (km)"], tablefmt="pretty")
print(taulukko)
