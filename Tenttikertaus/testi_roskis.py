lasku = 2*4
print(lasku)
vaite = (2 == 4)
print(vaite)    #tulostuu False, koska lause on epätosi
vaite2 = (6 <= 11)
print(vaite2)   #tulostuu True, koska lause on tosi.
vaite3 = (2+1 == 5)
print(vaite3)           #False

print(2+1+3)    #tässä tulostuu tulos

user = input("Kerro nimesi: ")
hello_amount = int(input("Syötä tervehdysten lukumäärä: "))

for number in range(hello_amount):
    print(f"Hei {number + 1}. kerran, {user}!")

