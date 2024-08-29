# Tehtävä 3.4
# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.

# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

#KÄYTÄ JAKOJÄÄNNÖSTÄ: If-ehtoon - jos jakojäännös = 0, on x:llä jaollinen

year = int(input("Kerro vuosiluku: "))      #kysytään vuosiluku
four = (year % 4)                           #jaetaan luku neljällä, tuloksena jakojäännös

if (four == 0):                             #ehto: jos jakojäännös on 0


#vanha koodi, tee muutokset:
year = int(input("Kerro vuosiluku: "))      #kysytään vuosiluku
four = (year/ 4)                           #jaetaan vuosiluku neljällä

if (four.is_integer()):             #kokeillaan, onko luku jaollinen neljällä #ei tarvi olla == True !
    hundred = (year / 100)                  #vuosiluku jaetaan sadalla
    if (hundred.is_integer()):      #kokeillaan, onko vuosiluku jaollinen sadalla
        fourhundred = (year / 400)          #jaetaan vuosiluku 400:lla
        if ( (hundred.is_integer()) and (fourhundred.is_integer()) ):  #jos jaollinen 100 ja 400, mol. totta
            print("Vuosi on karkausvuosi.")
        else:                               #jos sadalla jaollinen luku ei ole jaollinen 400:lla
            print("Vuosi ei ole karkausvuosi.")
    else: print("Vuosi on karkausvuosi.")   #jos vuosiluku ei ole jaollinen sadalla, on silti karkausvuosi
else:
    print("Vuosi ei ole karkausvuosi.")     #jos vuosiluku ei ole jaollinen neljällä, ei ole karkausvuosi.