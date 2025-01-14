# Moduuli 11 - PERIYTYMINEN

# Periytyminen on olio-ohjelmoinnin mekanismi, jossa luokkien välille muodostetaan hierarkia:
# yksittäisestä luokasta = yliluokasta johdetaan sitä tarkentavia aliluokkia

# YLILUOKKA ja ALILUOKKA

# jos aliluokalla on samoja ominaisuuksia kuin yliluokalla, se voi periä ominaisuudet toiminnolla super().__init__
# lisäksi tulee merkitä sulkeisiin, mitä ominaisuuksia haluaa periä
# esim. super().__init__(etunimi, sukunimi)
# --> tämä silloin, kun luokka määritetään vain yhden pääluokan avulla

# METODIEN YLIKIRJOITTAMINEN:
# voi hakea esim. tulostuksen pääluokasta, ja lisätä siihen uuden tulosteen


# esimerkki - ohjelma käsittelee Työntekijä-olioita

class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))

for t in työntekijät:
    t.tulosta_tiedot()

#######
print()
#######

# toinen esim, jossa on aliluokkia (tuntipalkkainen ja kuukausipalkkainen):

class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    #def tervehdi(self):
    #    print("Aliluokka Tuntipalkkainen tervehtii sinua!")

    def tulosta_tiedot(self):
        # haetaan yliluokan printti
        super().tulosta_tiedot()
        # lisätään oma aliluokan printti
        print(f"Tuntipalkka: {self.tuntipalkka} €")

class Kuukausipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kuukausipalkka: {self.kuukausipalkka} €")

    #def tervehdi(self):
    #    print("Aliluokka Kuukausipalkkainen tervehtii sinua!")


työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))
t1 = työntekijät.append(Tuntipalkkainen("Ulla", "Sederlöf", 10))
#t1.tervehdi()
#print(t1.etunimi, t1.sukunimi, t1.tuntipalkka)
työntekijät.append(Kuukausipalkkainen("Matti", "Peltoniemi", 10000))


for t in työntekijät:
    t.tulosta_tiedot()

# MONIPERINTÄ - luokka määritetään kahden tai useamman luokan aliluokaksi


class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus


class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino


class Polkupyörä(Kulkuneuvo, Urheiluväline):
    def __init__(self, nopeus, paino, vaihteet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)

        self.vaihteet = vaihteet


pp = Polkupyörä(45, 18.7, 3)
print(pp.vaihteet)
print(pp.nopeus)
print(pp.paino)
