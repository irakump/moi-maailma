# Tehtävä 11.2
# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena
# akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita
# aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja
# akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123,
# 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta
# autojen matkamittarilukemat.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tunnit    # matka = nopeus * aika

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti        # kilowattitunteina

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko                  # litroina

autot = []

s = Sahkoauto("ABC-15", 180, 52.5)
autot.append(s)

p = Polttomoottoriauto("ACD-123", 165, 32.3)
autot.append(p)

s.nopeus = 150
p.nopeus = 100
s.kulje(3)
p.kulje(3)

for a in autot:
    print(f"Auto {a.rekisteritunnus} on kulkenut {a.kuljettu_matka} km.")
