# Tehtävä 9.3
# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5)
# kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, nopeuden_muutos):                                        #luodaan metodi
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + (self.nopeus * tunnit)  #matka=nopeus(km/h)*aika (h)

auto = Auto("ABC-123", 142, 60, 2000)   #asetetaan esimerkkiarvot
print(f"Rekisteritunnus on {auto.rekisteritunnus}, huippunopeus {auto.huippunopeus} km/h, "
      f"tämänhetkinen nopeus {auto.nopeus} km/h ja kuljettu matka {auto.kuljettu_matka} km.")

auto.kulje(1.5)                                                    #auto kulkee 1,5 tuntia nopeudella 60 km/h
print(f"Auton kulkema matka on {auto.kuljettu_matka:.0f} km.")
