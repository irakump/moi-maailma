# Tehtävä 4.5
# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

user = input("Syötä käyttäjätunnus: ")      #kysytään käyttäjätunnus
password = input("Syötä salasana: ")        #kysytään salasana
reps = 1                                    #luodaan muuttuja, toistot

while (user != "python" or password != "rules") and (reps < 5):   #toistetaan enintään 5 kertaa
        reps = reps + 1
        user = input("Syötä käyttäjätunnus: ")
        password = input("Syötä salasana: ")
if (user == "python" and password == "rules"):
    print("Tervetuloa")
else:
    print("Pääsy evätty")
