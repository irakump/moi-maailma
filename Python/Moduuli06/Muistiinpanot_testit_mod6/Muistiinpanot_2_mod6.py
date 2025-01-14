#vaihtuva määrä parametreja (muuttujassa)
# * -merkki muuttujan nimen edellä tekee siitä listan, jolloin riville 10 ei tarvitse muodostaa listaa

def calculate_sum2(*numbers):           #tähän voi syöttää kuinka monta tahansa lukua (rivillä 10)
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

print(calculate_sum2(2,3,8,1,9))

print()

# NIMETYT PARAMETRIT JA OLETUSARVOT (funktioiden erityispiirteitä):

# yksinkertainen laskin, jolle voi antaa 2-3 parametria (eli kolmas on vapaaehtoinen):
def calculate2(number1, number2, calc_type="sum"):      #oletustyypiksi on laitettu summa, jos ei kirjoita
    if calc_type == "sum":                              #..tyyppiin mitään
        return number1 + number2            #return None #oletustoiminnallisuus
    elif calc_type == "division":           #jakolasku
        return number1 / number2

print(calculate2(6.7, 2.3))
print(calculate2(6.7, 2.3, calc_type = "division"))
#voi vaihtaa myös järjestystä nimeämällä numerot:
print(calculate2(number2 = 6.7, number1 = 2.3, calc_type = "division"))
