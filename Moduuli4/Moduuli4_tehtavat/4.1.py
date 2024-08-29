# Tehtävä 4.1
# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

number = 0

while (number <= 1000):
    if (number % 3 == 0):        #ehto: luku on jaollinen kolmella, eli jakojäännös on 0
        print(number)
    number = (number + 1)       #lisätään lukuun 3, turhia numeroita ei tarvitse testata
