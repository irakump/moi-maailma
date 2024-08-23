# Tehtävä 2.4
# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

first = input("Kerro kokonaisluku: ")
second = input("Kerro toinen kokonaisluku: ")
third = input("Kerro kolmas kokonaisluku: ")

sum = int(first) + int(second) + int(third) #summa
multiplication = int(first) * int(second) * int(third)	#tulo

#lukujen keskiarvo: (a+b+c)/3
mean = (int(first) + int(second) + int(third)) /3   #keskiarvo

print(f"Lukujen summa on {sum}, tulo {multiplication} ja keskiarvo {mean}.")
