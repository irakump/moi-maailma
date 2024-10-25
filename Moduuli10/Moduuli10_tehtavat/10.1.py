# Tehtävä 10.1
# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
# tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit
# ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja
# sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros       # uusi hissi on alimmassa kerroksessa

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylin_kerros:
            kerros = self.ylin_kerros
        elif kerros < self.alin_kerros:
            kerros = self.alin_kerros
        if kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros < kerros:
                self.kerros_ylos()
        elif kerros < self.nykyinen_kerros:
            while self.nykyinen_kerros > kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        self.nykyinen_kerros += 1
        print(f"Hissi on {self.nykyinen_kerros}. kerroksessa.")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Hissi on {self.nykyinen_kerros}. kerroksessa.")

# pääohjelma
h = Hissi(1, 10)
h.siirry_kerrokseen(7)
h.siirry_kerrokseen(1)
