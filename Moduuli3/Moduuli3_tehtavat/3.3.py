# Tehtävä 3.3
# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

gender = input("Kerro biologinen sukupuoli (nainen/mies): ")          #kysytään sukupuoli
hemoglobin_value = float(input("Kerro hemoglobiiniarvo (g/l): "))     #kysytään hemoglobiiniarvo

if (gender == "nainen"):                        #nainen
    if (117 <= hemoglobin_value <= 175):        #normaali hemoglobiini 117-175 g/l
        print("Hemoglobiiniarvo on normaali.")
    elif (hemoglobin_value < 117):              #alhainen hemoglobiini < 117 g/l
        print("Hemoglobiinarvo on alhainen.")
    else:                                       #muu (eli korkea hemoglobiini > 175 g/l)
        print("Hemoglobiiniarvo on korkea.")

if (gender == "mies"):                          #mies
    if (134 <= hemoglobin_value <= 195):        #normaali hemoglobiili 134-195 g/l.
        print("Hemoglobiiniarvo on normaali.")
    elif (hemoglobin_value < 134):              #alhainen hemoglobiini < 134 g/l
        print("Hemoglobiiniarvo on alhainen.")
    else:                                       #muu (korkea hemoglobiini > 195 g/l)
        print("Hemoglobiiniarvo on korkea.")
