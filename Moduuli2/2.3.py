# Tehtävä 2.3
# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

base = float(input("Syötä suorakulmion kanta (cm): "))   #kysytään kanta senttimetreinä
height = float(input("Syötä suorakulmion korkeus (cm): "))   #kysytään korkeus

#piirin kaava on kanta*2 + korkeus*2
#pinta-alan kaava on kanta*korkeus

circle = base*2 + height*2    #lasketaan suorakulmion piiri
area_rectangle = base*height   #lasketaan suorakulmion pinta-ala

print(f"Suorakulmion piiri on {circle} senttimetriä ja pinta-ala {area_rectangle} neliösenttimetriä.")
