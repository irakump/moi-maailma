# Tehtävä 10.3
# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
# hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

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


class Talo:
    hissi_lista = []

    def __init__(self, alin_krs, ylin_krs, hissit):
        self.alin_krs = alin_krs
        self.ylin_krs = ylin_krs
        self.hissit = hissit

        for hissi in range(hissit):
            hissi = Hissi(alin_krs, ylin_krs)
            self.hissi_lista.append(hissi)

    def aja_hissia(self, hissin_nro, kohdekerros):
        hissin_nro -= 1
        self.kohdekerros = kohdekerros
        print(f"Hissi {hissin_nro + 1} liikkuu.")
        self.hissi_lista[hissin_nro].siirry_kerrokseen(kohdekerros)
        return

    def palohalytys1(self):
        print("Palohälytys!!!")
        for h in self.hissi_lista:
            print(h.ylin_krs)
            print(f"{self.hissi_lista[0].hissin_nro}. hissi on {self.hissi_lista[0].kerros}. kerroksessa")
            if h.kerros > h.alin_krs:
                self.hissi_lista[h].siirry_kerrokseen(h.alin_krs)
            elif h.kerros == h.alin_krs:
                print("Hissi on jo alimmassa kerroksessa.")
        return

    def palohalytys(self):
        print("Palohälytys!!!")
        i = 1
        for i in range(1, self.hissit + 1):
            self.aja_hissia(i, self.alin_krs)
            #print(f"Hissi {i} on kerroksessa {self.hissi_lista[i-1].kerros}")

talo = Talo(1, 5, 4)
talo.aja_hissia(1, 4)
talo.aja_hissia(2, 3)
talo.aja_hissia(2, 10)
talo.aja_hissia(3,2)
talo.aja_hissia(4, 4)
talo.aja_hissia(4, 1)
talo.palohalytys()
