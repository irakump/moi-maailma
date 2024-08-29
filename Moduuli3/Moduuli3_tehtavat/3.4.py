# Tehtävä 3.4
# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.

# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

year = int(input("Kerro vuosiluku: "))              #kysytään vuosiluku

if (year % 4 == 0):                                 #vuosiluku on jaollinen neljällä
    if (year % 100 == 0) and (year % 400 != 0):     #vuosiluku on jaollinen sadalla, mutta ei neljälläsadalla
        print("Vuosi ei ole karkausvuosi.")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
