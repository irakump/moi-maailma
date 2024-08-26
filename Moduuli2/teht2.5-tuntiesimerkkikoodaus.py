# Tehtävä 2.5
# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
# Yksi leiviskä on 20 naulaa, yksi naula 32 luotia ja yksi luoti 13,3 grammaa.

#varmista, että käyttäjä antaa numeron (ei merkkijonoa)

leiviska = float(input("Anna leiviskät: "))   #pyydetään syöttämään leiviskät (ovat yleensä kokonaisia, voisi laittaa myös int)
naula = float(input("Anna naulat: "))      #pyydetään syöttämään naulat
luoti = float(input("Anna luodit: "))       #pyydetään syöttämän luodit

#ensin selvitetään, kuinka paljon on leivisköjä, nauloja ja luoteja (grammoina)

leiviska_gram = leiviska*20*32*13.3   #leiviskät grammoina
naula_gram = naula*32*13.3     #naulat grammoina
luoti_gram = luoti*13.3        #luodit grammoina

#lasketaan grammat yhteensä:
sum_gram = leiviska_gram + naula_gram + luoti_gram

kg = sum_gram/1000  #määrä kilogrammoina
#print("kokonais kg määrä on", kg)       #pilkulla voi erottaa muuttujat, ei tarvitse käyttää f-muotoa ( print(f"kokonais kg määrä on {kg}")

#int-komento pyöristää aina alaspäin! - antaa joskus virheellisen tuloksen

#jakojäännösoperaatio %, pelkän kokonaisosan palauttava jakolasku //

kg_kokonaisosa = int(sum_gram//1000)    #tässä lasketaan kokonaisten kilogrammojen osuus

g_jakojaannos = sum_gram % 1000    #grammojen jakojäännös

print(f"Massa nykymittojen mukaan on {kg_kokonaisosa} kg ja {g_jakojaannos:.2f} grammaa.") #2 desimaalin tarkkuudella grammojen vastaus

#pyöristääkö .2f-komento ylöspäin desimaalit = PYÖRISTÄÄ oikein pyöristyssäännön mukaan.