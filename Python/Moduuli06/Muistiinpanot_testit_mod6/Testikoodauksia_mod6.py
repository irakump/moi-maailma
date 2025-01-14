#Funktiot

def say_hello():            #luodaan funktio def-toiminnolla, jota seuraa funkt. nimi + ():
    print("Hello!")
    return              #funktio päättyy returniin

#funktio ei itsessään tee mitään, vaan sitä tulee kutsua.

print("Päivä alkaa terveyhdyksellä")
say_hello()                             #tässä kutsutaan funktiota - funktion nimellä
print("Sitten muihin hommiin.")

print()

#funktion määrityksen tulee olla koodissa ennen sen kutsumista, jotta ohjelma toimii

def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print ("Tervehditään lisää.")
tervehdi(2)

print()
