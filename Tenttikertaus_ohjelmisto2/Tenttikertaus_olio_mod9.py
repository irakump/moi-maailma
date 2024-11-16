# Tenttikertaus mod09 - olio

# Termit: LUOKKA, OLIO, METODI, ALUSTAJA (konstruktori), LUOKKAMUUTTUJA


# LUOKKA määrittää yhteiset ominaisuudet ja operaatiot OLIOILLE = luokan ilmentymille
# METODI = toiminto, esim. haukkuminen
# olioiden ominaisuudet voivat poiketa toisistaan
# ominaisuuksiin voidaan viitata olion_nimi.ominaisuus, esim. koira1.nimi
# luokkien nimet kirjoitetaan Isolla alkukirjaimella, esim. Koira tai KoiraHoitola (= "CamelCase")
# ALUSTAJA = konstruktori, asettaa automaattisesti halutut arvot luotavan olion ominaisuuksiksi
"""
Alustaja:
    def __init__(self, nimi, vuosi):
        self.nimi = nimi
        self.vuosi = vuosi
"""

# yllä: alustaja määritellään luokan sisällä kirjoittamalla funktio, jonka nimi on __init__
    # funktion ensimmäinen parametri on self, jonka jälkeen määritellään muut halutut parametrit
    # alustajan loppuun ei kirjoiteta return-lausetta.

# kun olio luodaan, ei kirjoiteta ollenkaan self-parametria
# luonti: koira = Koira("tähän-nimi", vuosi eli numero) eli: koira = Koira("Rekku", 2020)

# METODIT = toiminnot

class Koira:

    tehty = 0

    def __init__(self, nimi, vuosi, haukahdus="vuh vuh"):
        self.nimi = nimi
        self.vuosi = vuosi
        self.haukahdus = haukahdus
        Koira.tehty += 1    # lisätään muuttujaan luku 1

    def hauku(self):
        #print(self.haukahdus)
        print(f"{self.nimi} haukkuu: {self.haukahdus}")
        return

# voi antaa myös kerrat metodin parametrina:

    def hauku2(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return

koira1 = Koira("Köpi", 2018, "hau hau")
koira2 = Koira("Mörri", 2019)  # haukahdusta ei määritelty, joten tulee oletusarvo
koira3 = Koira("Viki", 2016, "WUUFFF WUUFFFF")
koira4 = Koira("Osku", 2023, "hhau")

koira2.hauku()
koira2.hauku2(4)
koira1.hauku2(3)
koira1.hauku()
koira3.hauku()
koira4.hauku()
print(f"Koiria on tehty: {Koira.tehty}")

# for i in range(5):
#    print("moi")
## yllä oleva tulostaa 5 kertaa moi, eli range on 0..4. Alkaa nollasta, ja päättyy ennen nroa 5

# metodin kutsu: olion-nimi.metodin-nimi("mahdolliset-parametrit")
# esim. koira2.hauku(3)     # pitäisi haukkua 3 kertaa.

# metodin sisällä voidaan viitata olion omiin ominaisuuksiin self.ominaisuuden-nimi, esim. self.haukahdus,
# viittaa kulloisenkin olion haukahdus-ominaisuuden arvoon

# LUOKKAMUUTTUJA = staattinen muuttuja
    # koko luokkaa koskeva tieto, joka ei liity mihinkään yksittäiseen luokan olioon
    # esim. kuinka monta koiraa eli koira-luokan ilmentymää on luotu
    # tehty = 0     # ennen alustajaa, ja kun luodaan uusi koira, voi luokkamuuttujaa kasvattaa yhdellä

# luokkamuuttujan arvoon viitataan Koira.tehty (luokan nimi . luokkamuuttujan nimi)
