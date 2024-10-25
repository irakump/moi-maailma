# Tehtävä 10.3
# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
# hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

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
        else:
            print(f"Hissi on jo {kerros} kerroksessa.")

    def kerros_ylos(self):
        self.nykyinen_kerros += 1
        print(f"Hissi on {self.nykyinen_kerros}. kerroksessa.")

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Hissi on {self.nykyinen_kerros}. kerroksessa.")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm

        # luodaan hissit
        self.hissit = []

        i = 0
        for i in range(hissien_lkm):
            h = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(h)
            i += 1
        print(f"Hissejä luotu {i} kpl")

    def aja_hissia(self, hissin_nro, kerros):
        self.hissin_nro = hissin_nro
        self.kerros = kerros
        print(f"\nHissi {hissin_nro}: ")
        hissi = self.hissit[hissin_nro - 1]
        hissi.siirry_kerrokseen(kerros)

    def palohalytys(self):
        print("\nPalohälytys!!!")

        i = 1
        for i in range(1, self.hissien_lkm + 1):
            self.aja_hissia(i, self.alin_kerros)
            i += 1
        print("\nKaikki hissit ovat alimmassa kerroksessa.")

# pääohjelma
talo = Talo(1, 12, 6)
talo.aja_hissia(1, 9)
talo.aja_hissia(1, 3)

talo.aja_hissia(6, 4)
talo.aja_hissia(3, 12)
talo.aja_hissia(3, 10)

talo.palohalytys()
