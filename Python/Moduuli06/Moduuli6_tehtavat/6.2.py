# Tehtävä 6.2
# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def roll_die(face):                             #luodaan muuttuja, face = tahko
    number = random.randint(1, face)
    return number

user_input = int(input("Syötä nopan tahkojen lukumäärä: "))
face = user_input                               #tallennetaan käyttäjän syöte muuttujaan
roll = roll_die(face)                           #kutsutaan funktiota 1. kerran, tallennetaan muuttujaan

while (roll != face):
    print(roll)
    roll = roll_die(face)                       #arvotaan uusi luku, kutsutaan funktiota
if (roll == face):
    print(roll)
