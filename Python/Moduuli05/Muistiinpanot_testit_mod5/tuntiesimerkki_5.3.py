# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

def is_prime_number(num):               #uusi muuttuja
    if num < 1:                         #jätetään nolla ja negatiiviset luvut testaamatta
        return False
    for i in range(2, num):
        #print(i)
        if num % i == 0:
            return False    #return katkaisee fuktion suorituksen, jos on jaollinen jollain i:n arvolla
    return True             #jos funktion suoritus jatkuu tänne asti, niin palautetaan True

#pääohjelma lukee syötteen ja tulostaa vastauksen:
user_input = int(input("Anna testattava luku: "))
if is_prime_number(user_input):                        # sama kuin: if is_prime_number == True:
    print(f"Luku {user_input} on alkuluku.")
else:
    print(f"Luku {user_input} ei ole alkuluku.")
