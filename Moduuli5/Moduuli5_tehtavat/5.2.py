# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
#
number = input("Kerro luku: ")          #merkkijono
numbers = []

while (number != ""):
    number = int(number)                #muutetaan merkkijono luvuksi
    numbers.append(number)              #lisätään luku listaan
    number = input("Kerro luku: ")      #kysytään uusi luku (merkkijono)

numbers.sort(reverse=True)              #järjestetään luvut suurimmasta pienimpään
print(f"Viisi suurinta lukua ovat {numbers[0]}, {numbers[1]}, {numbers[2]}, {numbers[3]} ja {numbers[4]}.")
