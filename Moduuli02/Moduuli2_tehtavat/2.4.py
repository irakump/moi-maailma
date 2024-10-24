# Tehtävä 2.4
# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

first = int(input("Kerro kokonaisluku: "))      #pyydetään käyttäjää syöttämään kokonaisluku
second = int(input("Kerro toinen kokonaisluku: "))
third = int(input("Kerro kolmas kokonaisluku: "))

sum = first + second + third    #lasketaan lukujen summa
multiplication = first * second * third     #lasketaan tulo

#lukujen keskiarvon kaava on (a+b+c)/3
mean = (first + second + third)/3   #lasketaan keskiarvo

print(f"Lukujen summa on {sum}, tulo {multiplication} ja keskiarvo {mean:.3f}.")    #rajataan ka:n desimaalit kolmeen
