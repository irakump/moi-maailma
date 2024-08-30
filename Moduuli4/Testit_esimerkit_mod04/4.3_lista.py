# Tehtävä 4.3 - käytetty listaa, jota ei vielä tässä moduulissa opeteta (mod5 tarkemmin)

# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän
# merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

numbers = []                            #luodaan tyhjä lista
number = input("Kerro luku: ")          #kysytään käyttäjältä luku (merkkijono)

while (number != ""):
    number = float(number)              #muutetaan merkkijono (liuku)luvuksi
    numbers.append(number)              #lisätään käyttäjän syöttämä luku listaan
    number = input("Kerro luku: ")

min_number = min(numbers)               #luodaan muuttujat: pienin ja suurin numero listasta
max_number = max(numbers)
print(f"Pienin luku on {min_number:.0f} ja suurin luku on {max_number:.0f}.")   #tulostus ilman desimaaleja
