# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

number = int(input("Syötä kokonaisluku: "))
numbers = []
iterator = 2

while (iterator <= number):
    numbers.append(iterator)            #lisätään iteraattori listaan
    iterator += 1

if (number == 0) or (number == 1):
    print("Luku ei ole alkuluku.")

for num in numbers:
    if (number % num == 0) and (number // num != 1):     #testataan, onko luku jaollinen muulla kuin itsellään
        print("Luku ei ole alkuluku.")
        break
    elif (number % num == 0) and (number // num == 1):   #luku on jaollinen vain itsellään (ja ykkösellä)
        print("Luku on alkuluku.")
