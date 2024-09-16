# Tehtävä 9.1
# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja
# kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina
# saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:                                                      #luodaan luokka
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

auto1 = Auto("ABC-123", 142)            #luodaan uusi auto ja asetetaan kaksi arvoa
print(f"Rekisteritunnus on {auto1.rekisteritunnus}, huippunopeus {auto1.huippunopeus} km/h, "
      f"tämänhetkinen nopeus {auto1.nopeus} km/h ja kuljettu matka {auto1.kuljettu_matka} km.")
