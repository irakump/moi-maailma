#Tenttikertausta

#MODUULI 3: valintarakenne (if)
#MODUULI 4: toistorakenne (while)

#Valintarakenne (if):

#if ehto:                               jos ehto on tosi, suoritetaan ehdollisesti suoritettava lohko
	#ehdollisesti suoritettava lohko

money = 3
if money >= 4:
    print(f"Voit ostaa latten, sinulla on {money} euroa.")
else:
    print("Rahasi eivät riitä laten ostamiseen.")


#######
print()
#######

#VERTAILUOPERAATTORIT:
# > suurempi kuin
# < pienempi kuin
# >= suurempi tai yhtäsuuri kuin
# <= pienempi tai yhtäsuuri kuin
# == yhtä suuri kuin                        #huomaa, on eri kuin =   ! Yhdellä = -merkillä merkitään muuttuja.
# != eri suuri kuin

#loogisia operaattoreita voi ketjuttaa, esim.      165 <= pituus <= 180

#LOOGISET OPERAATTORIT:
# and = ja, "molemmat"
# or = tai, "jompikumpi tai molemmat"
# not = ei, "ei"    (negaatio)

#loogisia operaattoreita voi käyttää esim. if-ehtolauseissa

#While-toistorakenne:

number = float(input("Kerro rahamäärä: "))
while number < 4:                                    #latte maksaa 4 e
    print("Anna lisää rahaa.")
    number = float(input("Kerro rahamäärä: "))
print("Nyt voit ostaa laten.")

#######
print()
#######

#esim2. while-toistorakenne, jossa tehdään itse kierrosmuuttuja
kerrat = int(input("Montako kertaa tervehditään: "))
tehdyt = 0
while tehdyt < kerrat:
    tehdyt = tehdyt + 1                 #sama kuin tehdyt += 1
    print(f"Hei {tehdyt}. kerran!")

#######
print()
#######

#satunnaislukugeneraattori random.randint - jatketaan, kunnes molemmista nopista saadaan luku 6.
import random
first_number = random.randint(1,6)       #luvut 1..6 eli 1, 2, 3, 4, 5 ja 6
second_number = random.randint(1,6)

while (first_number != 6) or (second_number != 6):
    print(f"Ekasta nopasta saatiin {first_number} ja tokasta {second_number}.")
    first_number = random.randint(1, 6)
    second_number = random.randint(1, 6)
print(f"Ekasta nopasta saatiin {first_number} ja tokasta {second_number}.")

#break-komennolla voi poistua ohjelmasta välittömästi

