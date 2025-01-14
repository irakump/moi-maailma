# Tehtävät 6.4
# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def sum_numbers(number_list):
    return sum(number_list)

odd_numbers = [1, 3, 5, 7, 9, 11, 13]           #luodaan lista
print(sum_numbers(odd_numbers))                 #kutsutaan funktiota, tulostetaan listan summa
