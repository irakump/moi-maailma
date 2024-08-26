#Pyöristyksiä: int pyöristää alaspäin, vaikka olisi esim. luku 2,6
#miten :.3f pyöristää ylöspäin pyöristyssäännön mukaisesti (esim. luku 2,66 on 2,7)

one = float(input("Kerro desimaaliluku: "))
two = float(input("Kerro toinen luku: "))
three = float(input("Kerro kolmas luku: "))

sum = one + two + three     #lukujen summa
print(sum)
print(f"Lukujen summa on {sum:.1f}.")   #summa yhden desimaalin tarkkuudella,
