# Moduuli 10 - assosiaatio

# Termit: ASSOSIAATIO, INSTANSSIMUUTTUJA, YKSISUUNTAINEN, KAKSISUUNTAINEN, PYSYVÄ, TILAPÄINEN

# ASSOSIAATIO = olioiden välinen tuntemissuhde - olio voi käsitellä toisia olioita ja kutsua niiden metodeja

# ohjelma voi koostua useammasta luokasta, ja luokat voivat olla eri tiedostoissa. Esim. file1 ja file2
# --> jos file1 viittaa tiedostoon file2, tulee file2 importoida file1-tiedostossa:
# import file2

# INSTANSSIMUUTTUJA = hoitola-oliolla on instanssimuuttuja, joka sisältää viittaukset Koira-olioihin

# YKSISUUNTAINEN ASSOSIAATIO = Hoitola-olio tietää, mitä koiria on hoidossa, mutta koira-olio ei tiedä mitään hoitolasta, jossa se (ehkä) on
# KAKSISUUNTAINEN ASSOSIAATIO = molemmat oliot tietävät toisistaan. Kannattaa toteuttaa vain silloin, kun sille on hyvät perusteet.

# PYSYVÄ ASSOSIAATIOSUHDE = suhde on pysyvä, esim. hoitolan koirat on tallennettu hoitolan ominaisuutena olevaan koiralistaan
# TILAPÄINEN ASSOSIAATIOSUHDE = olio annetaan toiselle oliolle vain parametrissa, mutta sitä ei tallenneta mihinkään
    # esim. auton ja maalaamon välinen suhde:

class Auto:
    def __init__(self, rekisteritunnus, vari):
        self.rekisteritunnus = rekisteritunnus
        self.vari = vari

class Maalaamo:
    def maalaa(self, auto, vari):           # tässä ei tehdä ollenkaan alustajaa (=konstruktoria, joten väri-parametri tai auto-p. ei tallennu!)
        auto.vari = vari

maalaamo = Maalaamo()
auto = Auto("ABC-123", "keltainen")
print(f"auton väri: {auto.vari}")
maalaamo.maalaa(auto, "vihreä")
print(f"auton väri: {auto.vari}")

# yllä on tilapäinen assosiaatiosuhde: maalaamo tuntee maalattavan auton vain maalaa-metodin suorituksen ajan (koska viittaus
    # Auto-olioon on saatu metodikutsun parametrina). Kun metodin suoritus päättyy, parametrimuuttujan arvoon ei enää pääse käsiksi.

    # auto ei tiedä maalaamosta mitään

############
print()
############



class Koira:

    tehty = 0

    def __init__(self, nimi, vuosi, haukahdus="vuh vuh"):
        self.nimi = nimi
        self.vuosi = vuosi
        self.haukahdus = haukahdus
        Koira.tehty += 1    # aina kun luodaan olio, luokkamuuttuja kasvaa yhdellä

    def hauku(self, kerrat):
        #self.kerrat = kerrat       # tätä ei tarvitse
        for i in range(kerrat):
            print(f"{self.nimi} haukkuu {i + 1}. kerran: {self.haukahdus}")
        return


class Hoitola:
    def __init__(self):
        self.koirat = []    # tyhjä lista koirille

    def koira_sisaan(self, koira):
        self.koirat.append(koira)           # lisätään koira listaan
        print(f"Hoitolaan saapui {koira.nimi}")
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(f"Hoitolasta lähtee {koira.nimi}")
        return

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.hauku(1)


koira1 = Koira("Rekku", 2022)
koira2 = Koira("Muhis", 2017, "Wwwhoooff")


hoitola = Hoitola()
hoitola.koira_sisaan(koira1)
hoitola.koira_sisaan(koira2)
hoitola.tervehdi_koiria()

hoitola.koira_ulos(koira1)
hoitola.tervehdi_koiria()

# muista lisätä jokaiseen luokan metodiin parametri self! esim. def hauku(self):        # ei toimi ilman self-parametria

