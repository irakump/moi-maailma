# Tehtävä 6.5
# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on
# muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä
# alkuperäisen että karsitun listan.

def delete_odd_numbers(list_name):
    for i in list_name:
        if (i % 2 != 0):
            list_name.remove(i)                     #poistetaan pariton luku listasta
    return list_name

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]           #luodaan lista
print(numbers)
print(delete_odd_numbers(numbers))                  #kutsutaan funktiota, tulostetaan karsittu lista
