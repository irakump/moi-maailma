# Tehtävä 7.1
# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
# vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

seasons = ("talvi", "kevät", "kesä", "syksy")                   #tallennetaan vuodenajat monikkoon merkkijonoina

month_number = int(input("Kerro kuukauden numero (1-12): "))    #kysytään käyttäjältä kuukautta vastaava numero

if ((1 <= month_number <= 2) or (month_number == 12)):
    print(f"Vuodenaika on {seasons[0]}.")
elif (3 <= month_number <= 5):
    print(f"Vuodenaika on {seasons[1]}.")
elif(6 <= month_number <= 8):
    print(f"Vuodenaika on {seasons[2]}.")
elif(9 <= month_number <= 11):
    print(f"Vuodenaika on {seasons[3]}.")
