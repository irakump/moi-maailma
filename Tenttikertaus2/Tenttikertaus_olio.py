class Kissa:
    def __init__(self, nimi, vuosi):
        self.nimi = nimi
        self.vuosi = vuosi

    def tervehdi(self):
        tervehdys = print(f"Moikkamoi")

        return tervehdys


kissa1 = Kissa("Miuku", 2018)
kissa1.tervehdi()
