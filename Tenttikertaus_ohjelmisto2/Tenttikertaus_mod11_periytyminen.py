# moduuli 10 - periytyminen

# termit: PERIYTYMINEN, YLILUOKKA, ALILUOKKA, METODIEN YLIKIRJOITTAMINEN, MONIPERINTÄ

# PERIYTYMINEN = olio ohjelmoinnin mekanismi, luokkien välille muodostetaan hierarkia. Yliluokasta johdetaan sitä tarkentavia
#   ja täsmentäviä luokkia eli aliluokkia

# super().__init__(ominaisuus)          --> tällä peritään, aliluokka perii yliluokan ominaisuudet. esim. super().__init__(etunimi, sukunimi)

# Yliluokka-aliluokkasuhde ilmaistaan Pythonissa siten, että aliluokan määrittävään class-lauseeseen lisätään sulkeisiin yliluokan
# nimi. Siis lauseen alku class Tuntipalkkainen(Työntekijä) määrää, että Tuntipalkkainen-luokasta tulee Työntekijä-luokan aliluokka.

# lause super().__init__(etunimi, sukunimi) kutsuu yliluokan alustajaa, joka saa parametreinaan etu- ja sukunimen

# METODIEN YLIKIRJOITTAMINEN = aliluokkaan luodaan toinen toteutus yliluokassa olevasta metodista. Kun kutsutaan aliluokan ilmentymän metodia,
# tulee "ylikirjoitettu" versio eli aliluokassa oleva metodi, sillä se "menee yliluokan metodin edelle"
# esim. t on Tuntipalkkainen-luokan ilmentymä.      t.tulosta_tiedot()  kutsuu Tuntipalkkainen-luokassa olevaa metodia tulosta_tiedot()
# yliluokan metodista voi olla useita muunnelmia aliluokissa. Kun loopissa tulostetaan kaikki listan tiedot, saavat oliot omat "sopivat" arvonsa
# esim. for t in työntekijät:
#           t.tulosta_tiedot()

# MONIPERINTÄ = sama luokka määritetään kahden tai useamman luokan aliluokaksi. esim. 2 luokkaa: Urheiluväline, Kulkuneuvo. Molempien aliluokka:
# Polkupyörä

# yliluokkaan viittaus moniperinnässä: pitää käyttää:   Yliluokka.__init__(self, ominaisuus)    esim. Urheiluväline.__init__(self, paino)
# ei voi käyttää super(). -funktiota, koska silloin periminen haetaan järjestyksessä vain ensimmäisestä luokasta, mikä ei toimi.

# tavallisessa perimisessä voi käyttää: super().__init__(ominaisuus)        --> ei tarvitse olla (self, ominaisuus)

class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino

class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus

class Polkupyörä(Urheiluväline, Kulkuneuvo):           # määritetään kahden luokan aliluokaksi
    def __init__(self, paino, nopeus, vaihteet):
        Urheiluväline.__init__(self, paino)                           # tässä pitää määritellä, mistä yliluokasta peritään!
        Kulkuneuvo.__init__(self, nopeus)                             # aina pitää periä myö self!! (moniperinnässä)
        self.vaihteet = vaihteet

pp = Polkupyörä(24, 19.5, 3)
print(pp.paino)
print(pp.nopeus)
print(pp.vaihteet)


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
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)                         # tässä kutsutaan yliluokan alustajaa __init__, yliluokan kutsumisen tunnistaa super(). -kohdasta

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")

class Kuukausipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()                            # myös metodeja voi periä. super().metodin-nimi
        print(f" Kuukausipalkka: {self.kuukausipalkka}")

työntekijät = []
tekijä1 = Tuntipalkkainen("Viivi", "Virta", 12.35)
työntekijät.append(tekijä1)
työntekijät.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
työntekijät.append(Työntekijä("Pekka", "Puro"))
työntekijät.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

tekijä1.tulosta_tiedot()        # tämä tulostaa olion tiedot

for t in työntekijät:
    t.tulosta_tiedot()




