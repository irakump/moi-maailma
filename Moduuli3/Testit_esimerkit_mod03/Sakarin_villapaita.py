#if-ehtorakenne, testi.

#Pue Sakarille villapaita.

villapaita = input("Pue Sakarille villapaita - kirjoita kyllä/en: ")

if villapaita == "kyllä":
    print("Voitit pelin!")
elif villapaita == "en":
    print("Hävisit pelin!")
else:
    print("Virheellinen vastaus.")

print("Peli päättyi.")