# MODUULI 6: FUNKTIOT

# Funktioita käyttävä ohjelma jakautuu:
# -pääohjelmaan eli siihen ohjelman osaan, joka sijaitsee funktioiden ulkopuolella
# -funktioihin.

# nimeäminen: jos nimi on kaksiosainen, laita ala_viiva
# funktioita mm. print, sort, random.randint, ...

#funtio on muodossa do_something() --> sulkeista tunnistaa, että kyseessä on funktio

"""
#esim1. määritellään oma funktio:  def-käskyllä
def do_something():
    print("Doing ")
    print("something")
    return                 #palauttaa jonkun arvon (esim. nyt tyhjänä tulostuu arvo None). Voisi laittaa
                            #esim. return
                            #tai merkkijonon esim. "tässä on palautettava arvo"

return_value = do_something()
print(return_value)
"""

# do_something()        #KUTSUTAAN funktiota (nimi ja sulkeet), niin tapahtuu funktioon määritelty asia


"""
#esim2. vaihdetaan return-sanan paikkaa
#return-sanan käyttö pysäyttää koodin suorittaminen
def do_something():
    print("Doing "
    return
    print("something")      #tätä ei suoriteta
"""
#return-funktiolla on kaksi tarkoitusta: palauttaa _joku_ arvo tai keskeyttää koodin suoritus

#esim3. - funktio, jolla on parametreja (argumentti)
def combine_string(string1, string2):        #sulkeiden sisällä määritellään lähtöarvot
    combination = f"{string1}, {string2}"      #funktiota ei voi jättää tyhjäksi, eli tulee olla sisälohko
                                            #voi olla myös pass - "passaa vuoron" tai jättää tekemättä
    return combination

print(combine_string("auto", "ajaa"))    #ensin ajetaan combine_words-muuttuja, sitten tulostus

combination = combine_string("kuski", "jarruttaa")
combination = combine_string(combination, "nopeasti")
print(combination)

#nimiä voi muuttaa samalla kertaa - valitse nimi/ maalaa - refactor
#nimeä funktio aina funktion mukaan, esim. calculate, print = VERBI

print()

#esim4. - yksinkertainen laskin, jolle voi antaa vain _tasan_ kaksi parametria
def calculate(number1, number2):
    return number1 + number2        #palauttaa lukujen summan

print(calculate(2.4, 3.5))
#print(calculate(2.4))      #antaa virheen, koska on vain yksi parametri. Samoin virhe, jos on 3 parametria.
print(calculate(6.7, 2.3))

print()

#esim5. - laskurin sisälle tyyppi, laskurille voi antaa tasan 3 parametria.
def calculate(calc_type, number1, number2):
    if calc_type == "sum":
        return number1 + number2            #return None #oletustoiminnallisuus
    elif calc_type == "division":           #jakolasku
        return number1 / number2

print(calculate("sum",6.7, 2.3))
print(calculate("division", 67, 3))

#jos on paljon sisennettyjä asioita esim. while-silmukassa: voi pilkkoa asioita funktioihin
#ks. opettajan esimerkit / github mod6, jossa muokattu noppa-muuttujaa, joka tehty aiemmasta moduulista

#LISTAT JA FUNKTIOT:

print()
"""
#esim6. - miten voi syöttää n määrän arvoja funktioon: käytä listaa
def calculate_sum(numbers):             #yksi parametri, johon voi syöttää listan
    total_sum = 0
    for i in range(len(numbers)):              #jos range on esim. 3: käydään läpi alkiot 0, 1, 2. Nyt n alkiota
        total_sum = total_sum + numbers[i]
    return total_sum

numbers = [3, 4, 5, 10, 1]
print(calculate_sum(numbers))
"""
print()

#esim7. - parempi vaihtoehto for-systeemiin:
def calculate_sum(numbers):                     #def on muuttuja, numbers on muuttujan nimi
    total_sum = 0

    for number in numbers:                  #listat nimetään monikkona. For-loopissa käytetään sanaa yksikkönä
        total_sum = total_sum + number      #voisi olla myös mikä tahansa nimi, kyseessä muuttujan nimi.
    return total_sum

nums = [3, 4, 5, 10, 1]                  #tämä on "pääohjelma", jonka sisällä käytetään muuttujaa
print(calculate_sum(nums))

#rivillä 99: number-kohdassa lisätään joka kierroksella kyseisessä alkiossa (listassa) oleva luku.
#1. kierroksella alkio 0 eli 3, 2. kierroksella alkio 1 eli 4...

#funktio palauttaa aina jotakin - oletusarvona on None. Eli pitää määritellä, jos haluaa jotakin tiettyä
#palauttaa, esim. tulosteen

#kun funktiota kutsutaan, esim. rivillä 103 - nums sijoitetaan muuttujaan numbers, jolloin muuttuja
#..calculate_sum pyörii listan luvuilla: 3, 4, 5, 10, 1


