# 10.1
# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
# siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h
# esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta
# kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai
# alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
# ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin_krs, ylin_krs, kerros=0):
        self.alin_krs = alin_krs
        self.ylin_krs = ylin_krs
        self.kerros = kerros

    def siirry_kerrokseen(self, kerros):
        if (kerros > self.ylin_krs):
            kerros = self.ylin_krs
        elif (kerros < self.alin_krs):
            kerros = self.alin_krs
        if (kerros > self.kerros):
            while (kerros > self.kerros):
                self.kerros_ylos()
                print(f"Hissi on {self.kerros}. kerroksessa")
        elif (kerros < self.kerros):
            while (kerros < self.kerros):
                self.kerros_alas()
                print(f"Hissi on {self.kerros}. kerroksessa")
        return

    def kerros_ylos(self):
        self.kerros += 1
        return

    def kerros_alas(self):
        self.kerros -= 1
        return


h = Hissi(0, 5)
h.siirry_kerrokseen(5)

h.siirry_kerrokseen(-2)
h.siirry_kerrokseen(13)
h.siirry_kerrokseen(2)
