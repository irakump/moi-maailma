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

#number = float(input("Anna luku: "))

#if number > 0:
#    print("Luku on positiivinen.")

#if number < 0:
#    print("Luku on negatiivinen.")

#if number == 0:
#    print("Luku on nolla.")     #aina 4 välilyöntiä

#pitkä kommentti: """ tähän tekstiä """

#Parempi tapa if-muuttujaan - yleensä ei käytetä pelkkää ifiä.

#else-haara - KAKSI toisensa poissulkevaa vaihtoehtoa:

#money = float(input("Kerro paljonko sinulla on rahaa: "))

#if money >= 5:  #enemmän tai yhtä suuri kuin 5
#    print("Voit ostaa latten, sinulla on tarpeeksi rahaa.")
#else:
#    print("Sinulla ei ole tarpeeksi rahaa latteen.")

#else: eli jos tulee mikä tahansa muu vaihtoehto kuin >= 5, niin elsen tulostus toteutuu, eli jos vastaus on false.

#MONTA VAIHTOEHTOA:
#user_input = input("Valitse a, b tai c: ")
#on mahdollista tehdä komento, joka muuttaa ison kirjaimen pieneksi.
#if user_input == "a":
#    print("Tehdään jotain, käyttäjä valitsi kirjaimen a")
#elif user_input == "b":
#    print("Tehdään toinen juttu, käyttäjä valitsi b")
#elif user_input == "c":
#    print("Käyttäjä valitsi c, tapahtuu x asia")
#    print("Saat c-luokan hytin.")
    #lohkossa voi olla paljon koodia, useita tulosteita, kaikki sisennetty suoritettaan.
#else:
#    print("Käyttäjä ei syöttänyt a, b tai c. Ohjelma ei toimi.")

#print("Ohjelma loppuu, hei hei!")

#LOOGISET OPERAATTORIT:
# and (ja/molemmat)
# or (tai)
#not (ei)

ika = 5
nimi = "Matti"

#lauseke a ja b on tosi täsmälleen silloin, kun sekä lause a että lause b ovat tosia.

#True True
print(ika < 10 and nimi == "Matti")     #jos molemmat ovat totta, tulostuu true.

#True False
print(ika < 10 and nimi == "Keijo")     #jos vain toinen toteutuu, tulostuu false.

#False False
print(ika < 2 and nimi == "Keijo")      #molemmat väärin, tulostuu false.

#OR:
#lauseke a or b on tosi täsmälleen silloin, kun vähintään jompi kumpi on totta.
print(ika < 10 or nimi == "Keijo")

