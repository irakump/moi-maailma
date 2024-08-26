#Pyöristyksiä: int pyöristää alaspäin, vaikka olisi esim. luku 2,6
#miten :.3f pyöristää ylöspäin pyöristyssäännön mukaisesti (esim. luku 2,66 on 2,7)

#one = float(input("Kerro desimaaliluku: "))
#two = float(input("Kerro toinen luku: "))
#three = float(input("Kerro kolmas luku: "))

# sum = one + two + three     #lukujen summa
#print(sum)
#print(f"Lukujen summa on {sum:.1f}.")   #summa yhden desimaalin tarkkuudella,

##################################
#Mod03 VALINTARAKENNE (IF)
#money = float(input("Kerro paljonko sinulla on rahaa: "))

#if money >= 5:  #enemmän tai yhtä suuri kuin 5
    #print("Voit ostaa latten, sinulla on tarpeeksi rahaa.")
    #lohko sisennetään aina 4 tyhjällä välimerkillä, kaksoispisteen jälkeen tulee automaattinen sisennys
#ehto on aina true tai false.

#yllä oleva on sama kuin:
#ehto = money >= 5
#print(ehto)

# ''' -merkeillä saa pidemmän pätkän kommentteihin


#if money < 5:
   # print("Et voi ostaa lattea, rahasi eivät riitä.")

'''money = float(input("Anna rahamääräsi: "))

ehto = (money >= 5)
print(ehto)
if ehto:
    #tämä osa on lohko ja suoritetaan, jos ehto on totta
    print("Voit ostaa latten, sinulla on tarpeeksi rahaa.")

#consolessa voi kokeilla true/false-toimintoa (bool)
# A = true (tee muuttuja)
#B = False
#kokeile: 5 < 3     -tulostaa false
# 5 > 3         -tulostaa true
# 5 == 3        # == yhtä suuri kuin (ei riitä pelkkä = !)
# = merkillä laitetaan muuttuja
#"moi" == "moi"         -true
# "moi" == "MOI"        -false
# != eri suuri kuin
'''
#esimerkki2:
#suutari = input("Anna suutarin nimi: ")
#räätäli = input("Anna räätälin nimi: ")

#if suutari == räätäli:
#    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")

#if suutari != räätäli:
#    print("Suutarilla ja räätälillä on eri nimet.")

#Tehtävä: luo ohjelma, joka pyytää käyttäjältä numeron ja tulostaa onko luku pos, neg vai nolla. (käytä vain if-ehtoa).

number = float(input("Anna luku: "))

if number > 0:
    print("Luku on positiivinen.")

if number < 0:
    print("Luku on negatiivinen.")

if number == 0:
    print("Luku on nolla.")

#pitkä kommentti: """ tähän tekstiä """

