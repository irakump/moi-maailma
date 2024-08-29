# Tehtävä 4.2
# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

inch = float(input("Kerro tuumat: "))   #kysytään tuumamäärä

while (inch >= 0):
    inch = inch * 2.54  # lasketaan tuumat senttimetreinä
    print(f"Tuumat senttimetreiksi käännettynä: {inch:.2f}.")   #kahden desimaalin tarkkuudella
    inch = float(input("Kerro tuumat: "))  # kysytään tuumamäärä
