# JOUKKO eli set {}

"""
-Joukko on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.
-Koska järjestystä ei ole määritelty alkioille, ei niihin voi viitata indeksillä
-Joukossa sama alkio (esim. luku 6) voi esiintyä vain yhden kerran. Vertaa: listassa ja joukossa voi
    esiintyä useamman kerran, esim. listassa: [6, 6, 6, 7]

-Jos haluaa varmistaa, että alkio esiintyy vain yhden kerran, kannattaa käyttää joukkoa
"""

#esim1. Luodaan joukko:
my_set = {1, 2, 3, 4, 5, 6}     #joukko merkataan aaltosulkeilla
print(my_set)

print()

#lista, jossa useampi sama alkio:
print(f"Numero 6 voi esiintyä listassa useasti: ")
my_list = [1, 2, 3, 4, 5, 6, 6, 6, 7]
print(my_list)

print()

#monikko:
print(f"Numero 6 voi esiintyä monikossa useasti: ")
my_tuple = (1, 2, 3, 4, 6, 5, 6, 7, 6)
print(my_tuple)

print()

#joukko:
print(f"Numero 6 EI voi esiintyä joukossa useasti: ")
my_set = {6, 1, 2, 3, 6, 5, 6}
print(my_set)           #joukko tulostaa numeron 6 vain yhden kerran. Joukossa ei ole järjestystä!

#yllä oleva ei tuota virhettä. Myöskään add-metodi ei tuota virhettä, jos yrittää lisätä saman alkion,
    #joka on jo listassa.
print()

print("Yritetään lisätä joukkoon sama alkio")
my_set.add(6)
print(my_set)

my_set.add(7)       #lisätään uusi alkio
print(my_set)

print()

#luodaan joukko ja tulostetaan sen alkiot erikseen for-silmukan avulla (edelleenkään ei ole järjestystä)
games = {"shakki", "monopoly", "mario kart", "uno"}
for g in games:
    print(g)

print()

print(f"Joukko on: {games}.")           #jos tulostaa joukon useasti, järjestys vaihtuu.

print()

#joukkoa ja sanakirjaa pystyy muokkaamaan, samoin kuin listaa.
#Monikkoa ei pysty muokkaamaan.

#koodiesimerkki materiaalista - järjestys voi muuttua printatessa:
pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")       #lisätään peli
print(pelit)                #tulostetaan joukko

pelit.remove("Shakki")      #poistetaan shakki joukosta
print(pelit)                #tulsotetaan joukko

#pelit.add("Cluedo")         #yritetään lisätä Cluedo, mutta joukkoon ei voi lisätä samaa alkiota
#print(pelit)                #tulostetaan taas

print()

for p in pelit:             #tulostetaan for/in -rakenteella joukon jäsenet, iteroidaan joukko
    print(p)
    if (p == "Cluedo"):         #testataan, onko joukossa Cluedo-peli ja jos on, tulostetaan
        print("Cluedo löytyi!")

print()

#sama eri tavalla: if/in        #if / in -haku toimii kuten listoissa
if "Monopoli" in pelit:
    print("Monopoli löytyi!!!")

print()

#tyhjää joukkoa ei voi luoda pelkkien kaarisulkeiden avulla (koska syntyy sanakirja!)
autojoukko = {}
print(autojoukko)
print(type(autojoukko))         #tulostuu: <class 'dict'>  #eli tyyppi on sanakirja!

#luodaan tyhjä joukko set:in avulla:
car_set = set()
car_set.add("Audi")             #lisätään alkio joukkoon
car_set.add("Lada")
print(type(car_set))            #kokeillaan, mikä on joukon tyyppi: <class 'set'>
print(car_set)


