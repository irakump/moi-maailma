# Tehtävä 9.1
# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden
# auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton
# (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka


auto = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus: {auto.rekisteritunnus}\nhuippunopeus: {auto.huippunopeus} km/h\ntämänhetkinen nopeus: "
      f"{auto.tamanhetkinen_nopeus} km/h\nkuljettu matka: {auto.kuljettu_matka} km")
