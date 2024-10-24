# Tehtävä 4.4
# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random
number = random.randint(1,10)                 #tietokone arpoo luvun väliltä 1..10

guess = int(input("Arvaa numero väliltä 1..10: "))  #käyttäjän arvaus
while (guess != number):
    if (guess < number):
        print("Liian pieni arvaus")
    else:                                           #(guess > number)
        print("Liian suuri arvaus")
    guess = int(input("Arvaa numero: "))            #päivitetään käyttäjän arvaus
print("Oikein")
