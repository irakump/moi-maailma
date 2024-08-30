# Tehtävä 4.3
# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän
# merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

numbers = []                            #luodaan tyhjä lista

number = input("Kerro luku: ")          #kysytään käyttäjältä luku (merkkijono)

while (number != ""):
    number = int(number)                #muutetaan merkkijono kokonaisluvuksi
    numbers.append(number)              #lisätään käyttäjän syöttämä luku listaan
    number = input("Kerro luku: ")

min_number = min(numbers)               #luodaan muuttujat: pienin ja suurin numero listasta
max_number = max(numbers)
print(f"Pienin luku on {min_number} ja suurin luku on {max_number}.")

#jos luvuissa esim. 500 ja 88, ohjelma tunnistaa, että 88 on suurempi?? (johtuu merkkijonosta, koska
# tutkii niitä aakkosjärjestyksessä) --> tämä ilman int-muutosta rivillä 10.
