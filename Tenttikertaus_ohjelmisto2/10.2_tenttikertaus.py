# Tehtävä 10.2
# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman
# ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan
# hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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

        for h in range(hissit):
            hissi = Hissi(alin_krs, ylin_krs)
            self.hissi_lista.append(hissi)

    def aja_hissia(self, hissin_nro, kohdekerros):
        hissin_nro -= 1
        self.kohdekerros = kohdekerros
        print(f"Hissi {hissin_nro + 1} liikkuu.")
        self.hissi_lista[hissin_nro].siirry_kerrokseen(kohdekerros)
        return


talo = Talo(1, 5, 2)
talo.aja_hissia(1, 4)
talo.aja_hissia(2, 3)
talo.aja_hissia(2, 10)
talo.aja_hissia(1,2)

