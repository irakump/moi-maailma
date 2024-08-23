# Tehtävä 2.3
# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

base = input("Kerro suorakulmion kanta: ")
height = input("Kerro suorakulmion korkeus: ")

#piirin kaava on kanta*2 + korkeus*2
#pinta-alan kaava on kanta*korkeus

circle = float(base)*2 + float(height)*2    #suorakulmion piiri
area_rectangle = float(base)*float(height)   #suorakulmion pinta-ala

print(f"Suorakulmion piiri on {circle} ja pinta-ala {area_rectangle}")
