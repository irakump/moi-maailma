# Tehtävä 6.3
# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa
# paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä
# aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def change_gallons_to_litres(gallon):
    litre = (gallon * 3.758)                                                    #muutetaan gallonat litroiksi
    return litre

user_input = float(input("Kerro bensiinin määrä gallonoina: "))
gallon = user_input

while (gallon >= 0):
    print(f"Bensiinin määrä litroina: {change_gallons_to_litres(gallon):.3f}")  #kutsutaan funktiota
    user_input = float(input("Kerro bensiinin määrä gallonoina: "))
    gallon = user_input
