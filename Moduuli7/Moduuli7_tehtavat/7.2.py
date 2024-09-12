# Tehtävä 7.2.
# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

name_set = set()                            #luodaan tyhjä joukko
user_input = input("Syötä nimi: ")          #kysytään nimi ensimmäisen kerran

while (user_input != ""):                   #kysytään nimiä (tyhjään merkkijonoon saakka), ehtoon sopiva tuloste
    if user_input in name_set:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    name_set.add(user_input)                #lisätään uusi nimi joukkoon, aiemmin lisätyt eivät tallennu
    user_input = input("Syötä nimi: ")

for n in name_set:                          #käydään läpi joukko ja tulostetaan nimet yksitellen
    print(n)
