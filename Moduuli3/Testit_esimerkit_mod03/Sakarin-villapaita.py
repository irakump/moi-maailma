#if-ehtorakenne, testi

#Pue Sakarille villapaita.

villapaita = input("Pue Sakarille villapaita - kirjoita kyllä/en: ")

if villapaita == "kyllä":
    print("Voitit pelin!")
elif villapaita == "en":
    print("Hävisit pelin!")
else:
    print("Ääliö, sinun tulee valita kyllä tai en.")
    print("Yritä uudestaan.")

print("Peli päättyi.")