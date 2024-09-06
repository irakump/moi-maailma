# Tehtävät 6.4
# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

# Tehtävä ilman sum-funktiota

def sum_numbers(number_list):
    result = 0
    for i in number_list:
        result = result + i
    return result

odd_numbers = [1, 3, 5, 7, 9, 11, 13]
print(sum_numbers(odd_numbers))
