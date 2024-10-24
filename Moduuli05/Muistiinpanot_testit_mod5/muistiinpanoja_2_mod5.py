#FOR-TOISTORAKENNE:

nimet = []

etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while etunimi != "":
    nimet.append(etunimi)
    etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for nimi in nimet:                  #for-toistorakenteella voi tehdä saman kuin while-silmukalla
    print (f"Moi, {nimi}!")

print("")

for kirjain in "abcde":         #voi käydä yksittäin merkkijonon kirjaimet läpi
    print(kirjain)

print("")

for alkio in [1, 2, 3, 4, 5]:
    print(alkio)

#iterator = kierrosmuuttuja

names = ["Aaro", "Bee", "Cecilia", "Daniel", "Elf"]
for nimi in names:
    print(nimi)

print("")

#RANGE-funktio:         (range = alue)

for numero in range(3,11):       #luvut väliltä 1-11
    print(numero)               #tulostuu kaikki luvut annetulta väliltä (range), viimeistä ei oteta mukaan
                                #eli tulostuu 3-10
print("")

for i in range(99, 0, -3):     #takaperin joka 3. luku
    print(i)

print("")

#käytetään edellä olevia iteroimaan nimilistaa läpi (iteroida = käydä läpi)

#for-silmukka iteraattorilla

print(names)
for i in range(3):      #kolme ensimmäistä nimeä    #0, 1, 2
    print(i)
    print(f"Terve, {names[i]}")     #range tarjoaa vain numeroita, pitää viitata listan alkioihin lista[]

print("")

#esim. - range, tervehditään kaikkia


for i in range(len(names)):            #len-funktiolla voi tulostaa listan pituuden maksimina
    print(f"Terve, {names[i]}")

print("")

#yllä olevan voisi tehdä myös:
listan_pituus = len(names)
print(f"Lista on {listan_pituus} alkiota pitkä")

for i in range(listan_pituus):
    print(f"Terve, {names[i]}")

