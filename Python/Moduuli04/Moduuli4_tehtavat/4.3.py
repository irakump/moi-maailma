# Tehtävä 4.3
# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän
# merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

number = smallest_number = biggest_number = input("Kerro luku: ")     #kysytään luku (merkkijono)

while (number != ""):
    number = int(number)                    #muutetaan merkkijono luvuksi
    if number > int(biggest_number):
        biggest_number = number             #tallennetaan isompi luku muuttujaan
    elif number < int(smallest_number):
        smallest_number = number            #tallennetaan pienempi luku muuttujaan
    number = input("Kerro luku: ")
print(f"Pienin luku on {smallest_number} ja suurin luku on {biggest_number}.")
