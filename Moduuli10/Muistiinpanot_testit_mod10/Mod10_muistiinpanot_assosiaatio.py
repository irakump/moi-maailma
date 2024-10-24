# Moduuli 10 - assosiaatiot

# kaksi luokkaa voi yhdistää

# tehdään kaksi luokkaa: auto ja kuljettaja. Tässä tapauksessa kuljettajalla on auto, eli pitää valita
# miten luokat yhdistetään toisiinsa (voisi olla myös niin, että autolla on kuljettaja)

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

    def tulosta_ominaisuudet(self):
        print(f"Rekkari: {self.rekisteritunnus}, huippunopeus: {self.huippunopeus} km/h, "
              f"tämänhetkinen nopeus: {self.nopeus} km/h.")

class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

    def aja(self):
        print(f"Olen {self.nimi}, {self.ika} vuotta ja ajan autoa {self.auto.rekisteritunnus}.")
        print("Ajetaan autoa.")
        self.auto.kiihdyta(40)
        print(f"Nopeus: {self.auto.nopeus} km/h")
        self.auto.kiihdyta(140)
        print(f"Nopeus: {self.auto.nopeus} km/h")
        self.auto.kiihdyta(-200)
        print(f"Nopeus: {self.auto.nopeus} km/h")


# luodaan kolmas luokka
class Autotalli:
    def __init__(self):
        self.autot = []             # luodaan tyhjä lista

    def auto_sisaan(self, auto):
        # tarkistetaan, ettei auto ole jo tallissa (parempi tapa: muuta lista joukoksi, jolloin ei ole duplikaatteja)
        for a in self.autot:
            if a == auto:       # --> True, jos viittaavat samaan olioon
                return          # tässä kohtaa poistutaan funktiosta
        self.autot.append(auto)

    def auto_ulos(self, auto):
        self.autot.remove()
        return                      # ???jos ei ole return, palauttaa None???

    def tulosta_inventaario(self):
        print("Autot tallissa: ")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()



# luodaan oliot ja sijoitetaan viittaukset niihin muuttujiin
auto1 = Auto("ABC-123", 180)
auto2 = Auto("TYU-345", 250)
auto3 = Auto("UIP-468", 150)
kuski = Kuljettaja("Räikkönen", 44, auto1)
kuski.aja()
kuski.auto = auto2
kuski.aja()

talli = Autotalli()
talli.auto_sisaan(auto1)
talli.tulosta_inventaario()
talli.auto_sisaan(auto2)
talli.auto_sisaan(auto3)
talli.tulosta_inventaario()

# nyt yllä oleva versio sallii saman auton laittamisen talliin useaan kertaan
    # muutokset: joko autolistasta tehdään joukko (jos autojen järjestyksellä ei ole väliä)


"""
# käytetään olion toimintoja nopeuden ja kuljetun matkan muuttamiseen (saman voi tehdä myös...
# ...konstruktorin sisällä)
auto1.kiihdyta(20)
auto2.kiihdyta(50)
auto1.kulje(1)
auto2.kulje(2)

print(f"Auto {auto1.rekisteritunnus}: huippunopeus {auto1.huippunopeus}, nopeus: {auto1.nopeus}, "
      f"kuljettu matka: {auto1.kuljettu_matka}")
print(f"Auto {auto2.rekisteritunnus}: huippunopeus {auto2.huippunopeus}, nopeus: {auto2.nopeus}, "
      f"kuljettu matka: {auto2.kuljettu_matka}")
"""

"""
esim. pass:

def auto_sisaan(self):
    pass                    # pass on tilapäinen, eli funktiota ei suoriteta (voisi olla myös return)
"""



