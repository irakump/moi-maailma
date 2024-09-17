#Tenttikertaus, moduuli 5

#Mod5 Listarakenne ja läpikäyvä toistorakenne (for)

#LISTARAKENNE JA LÄPIKÄYVÄ TOISTORAKENNE (FOR) - for sisältää kierrosmuuttujan:

#Lista tarkoittaa järjestettyä joukkoa alkioita.
my_list = []        #luodaan tyhjä lista
numbers = [2, 6, 3, 9, 1, 34, 4]     #luodaan lista, jossa on jo alkioita
names = ["Silvia", "Akseli", "Herbert", "Hunaja", "Potter", "Gandalf"]

print(names[0])     #tulostetaan names-listan 1. alkio - lista alkaa aina nollasta!
print(names[3])     #tulostuu listan 4. alkio
print(names[-1])    #tulostuu listan viimeinen alkio
print(names[-2])    #... toiseksi viimeinen alkio, eli lasketaan viimeisestä eteenpäin, alkaen -1
print(names)        #koko lista tulostuu (listamuodossa!)
print(names[2:])    #tulostuu 3. alkiosta alkaen listana, loppuun saakka
print(names[1:4])   #tulostuu listana 2. alkiosta alkaen, päättyen 3. alkioon (4. ei lasketa mukaan)

#listan pituus saadaan len-funktiolla:
print(len(names))       #tulostuu 6, joka on names-listan pituus
print(len(numbers))     #tulostuu 8
print(len(my_list))     #0, koska lista on tyhjä.

#######
print()
#######

#LISTAOPERAATIOT:
#append - lisää alkion listan loppuun
#remove - poistaa alkion ensimmäisen ilmentymän listasta
#insert - lisää alkion haluttuun kohtaan ennen alkiota, joka siinä paikalla jo on (esim. 2. indeksi)
#extend - liittää toisen listan ensimmäiseen listaan
#index - palauttaa alkion ensimmäisen sijainnin indeksin
#in - testaa, esiintyykö alkio listassa
#sort - lajittelee listan alkiot aakkos- tai suuruusjärjestykseen

#esim.
#names = ["Silvia", "Akseli", "Herbert", "Hunaja", "Potter", "Gandalf"]
names.append("Voldemort")   #lisätään alkio listan loppuun
print(names)
names.remove("Akseli")      #poistaa alkion listasta (jos niitä on useampi, poistaa ensimmäisen)
print(names)
names.remove(names[1])      #poistaa listasta 1. alkion eli toisen nimen, joka on Herbert.
print(names)

names.insert(3, "Hermione")     #asettaa nimen 3. indeksiin eli neljänneksi
print(names)
location = names.index("Potter")    #tallennetaan muuttujaan indeksikysely
print(location)                     #palauttaa indeksin 2, eli tuloste: 2

new_names = ("Hagrid", "Ksenofilius")   #luodaan uusi lista uusille nimille
names.extend(new_names)                 #lisään uusi lista vanhaan names-listaan
print(names)                            #tulostuu lista, jossa uudet nimet on listan viimeisenä

if "Matti" in names:                #in: kokeillaan, onko nimi listassa ja tehdään sopiva tulostus.
    print("Matti löytyi")
else:
    print("Nimeä Matti ei ole listassa.")

if "Voldemort" in names:
    print("Tiedät-kai-kuka on listassa.")
else:
    print("Pimeyden lordia ei löytynyt!")

names.sort()        #sort() järjestää listan aakkos- tai suuruusjärjestykseen.
print(names)
print(names[3])     #nyt 3. indeksi (eli 4. alkio) on Hunaja


numbers.sort()      #järjestää numerot pienimmästä suurempaan
print(numbers)

#######
print()
#######

#LISTAN LÄPIKÄYNTI FOR-RAKENTEELLA:
#ohjelma, joka kysyy käyttäjältä nimiä, kunnes hän syöttää tyhjän merkkijonon. Lopuksi tervehditään
#jokaista nimeä yksitellen.

names2 = []     #tyhjä lista
name = input("Kerro nimi tai lopeta painamalla enter: ")

while name != "":
    names2.append(name)
    name = input("Kerro nimi tai lopeta painamalla enter: ")

for n in names2:
    print(f"Hei, {n}!")

#RANGE-FUNKTIO: (toimii for-loopin kanssa)

#range-funtiolla voi määrittää halutut arvot:
#1. argumentti on välin alkupiste, 2. argumentti välin loppupiste (2 pistettä pakollista olla)
#3., valinnainen argumentti, on askeleen suuruus

#esim.
#luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for luku in range(3,10):    #tulostetaan luvut välillä 3..9 (rangessa määritellään, että on kyse luvuista)
    print(luku)

for number in range(3,10,3):    #luvut välillä 3..9, tulostuu 3 välein eli 3, 6, 9
    print(number)

for i in range(5,0,-1):         #3. argumentti: -1 --> saa laskevan järjestyksen eli 5,4,3,2,1
    print(i)

#esim. range(10,21,2) määrittää arvot 10, 12, 14, 16, 18, 20

for luku in range(6):
    print ("Moi!")      #tulostuu 6 kertaa merkkijono Moi!

