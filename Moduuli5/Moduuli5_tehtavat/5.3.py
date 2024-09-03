# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

number = int(input("Syötä kokonaisluku: "))

#jakojäännös %
#kokonaisosan palauttava jakojäännös //

#kaikki luvut jaollisia itsellään ja ykkösellä
#alkuluvut ovat jaollisia VAIN itsellään ja ykkösellä

if (number == 0) or (number == 1):
    print("Luku ei ole alkuluku.")


iterator = 2

#silmukka 1: tulostuu, jos luku ei ole alkuluku
while (iterator < number):
    if number % iterator == 0:             #jos jakojäännös on 0, luku on jaollinen muulla kuin 1 tai itsellään
        print("Luku ei ole alkuluku.")
    iterator += 1

#kokeile toimiiko for-ehdolla?

#silmukka 2:    tarkoitus saada tulostumaan, jos luku on alkuluku. Nyt tulostuu myös alkuluku esim. luvulle 4???
while (iterator <= number):
    if (number % iterator != 0):        #tarviiko tätä??
        continue
    if (number % iterator == 0) and (number // iterator != 1):
        break
    if (number % iterator == 0) and (number // iterator == 1):      #väärin
        print("Luku on alkuluku.")
    iterator += 1

#?????????????? kesken
#miten saa tulostumaan alkuluvut tekstillä "on alkuluku"???

#eka silmulla toimii