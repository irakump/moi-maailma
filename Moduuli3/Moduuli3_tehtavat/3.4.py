# Tehtävä 3.4
# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.

# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

year = int(input("Kerro vuosiluku: "))      #kysytään vuosiluku
four = (year/ 4)                           #jaetaan vuosiluku neljällä

if (four.is_integer() == True):             #kokeillaan, onko luku jaollinen neljällä
    hundred = (year / 100)                  #vuosiluku jaetaan sadalla
    if (hundred.is_integer() == True):      #kokeillaan, onko vuosiluku jaollinen sadalla
        fourhundred = (year / 400)          #jaetaan vuosiluku 400:lla
        if ((hundred.is_integer() == True) and (fourhundred.is_integer() == True)):  #jos jaollinen 100 ja 400
            print("Vuosi on karkausvuosi.")
        else:                               #jos sadalla jaollinen luku ei ole jaollinen 400:lla
            print("Vuosi ei ole karkausvuosi.")
    else: print("Vuosi on karkausvuosi.")   #jos vuosiluku ei ole jaollinen sadalla, on silti karkausvuosi
else:
    print("Vuosi ei ole karkausvuosi.")     #jos vuosiluku ei ole jaollinen neljällä, ei ole karkausvuosi

#yllä oleva toimii, mutta on varmasti parempi tapa ilman .is_integer() -komentoa???


#testi2:
"""
if (onko_kokoluku == True):             #jos vuosiluku on jaollinen neljällä:
    hundred = (year_first / 100)        #jaetaan sadalla
    if (hundred.is_integer() == True):      #jos luku on jaollinen sadalla:
        fourhundred = (year_first / 400):     #jaetaan vuosiluku 400:lla
            if (fourhundred.is_integer() == True):
                print("Vuosi on karkausvuosi.")     #tarviiko tätä ollenkaan?
print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
"""
#voisiko käyttää komentoja and, or?

#pitää testata, onko luku sadalla jaollinen JA? neljälläsadalla
#  if (year_first >= 100):  # jos vuosiluku on suurempi kuin sata, tehdään tämä

#lisää vielä testi, onko luku jaollinen sadalla.

#print(year.is_integer())    #tulostuu true, jos on kokonaisluku

#rivi 7: lasku antaa liukuluvun - ei voi muuttaa intiksi, koska silloin kaikki luvut olisivat kokonaislukuja.

"""
if(type(year) == int):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
"""
#print(type(year))   #tulostuu tyyppi: int/float

#if(year / 4):                               #selvitetään, onko vuosi jaollinen neljällä
    #print("Vuosi on karkausvuosi.")
#else:
    #print("Vuosi ei ole karkausvuosi.")

# year / 4 ei toimi. Tulee olla kokonaisluku (int)
# pitää selvittää lisäksi, onko vuosi jaollinen sadalla


"""
Selvitetään, onko luku int vai float:
i = 100
f = 1.23

print(type(i))
print(type(f))
# <class 'int'>
# <class 'float'>
"""

# print(f.is_integer())   #selvitetään, onko float-muotoinen luku kokonaisluku, esim. 10.0
#f on muuttuja
