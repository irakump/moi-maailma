# Tehtävä 2.5
# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa, yksi naula 32 luotia ja yksi luoti 13,3 grammaa.

print("Kerro massa keskiaikaisten mittojen mukaan.")
leiviskat = float(input("Anna leiviskät: "))    #float - muuttujasta tulee suoraan liukuluku
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leiviskat_grammoina = leiviskat*20*32*13.3  #lasketaan massa grammoina
naulat_grammoina = naulat*32*13.3
luodit_grammoina = luodit*13.3

sum_grammoina = leiviskat_grammoina + naulat_grammoina + luodit_grammoina   #massa yhteensä grammoina

kilogram = int(sum_grammoina*0.001)    #kilogrammat kokonaislukuna, 1 g = 0,001 kg.

gram_kokoluku = int(sum_grammoina - (kilogram*1000))  #1 kg = 1000 g. Grammat kokonaislukuna, vähennetään kg osuus (grammoina)

print(f"Massa nykymittojen mukaan on {kilogram} kilogrammaa ja {gram_kokoluku} grammaa.")

#Toinen tapa laskea sama asia:
gram_jakojaannos = int(sum_grammoina%1000)  #jakojäännös, kun jakaa koko massan 1 kilolla

#Koodi jakojäännöksen kanssa:

print("Kerro massa keskiaikaisten mittojen mukaan.")
leiviskat = float(input("Anna leiviskät: "))    #float - muuttujasta tulee suoraan liukuluku
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leiviskat_grammoina = leiviskat*20*32*13.3  #lasketaan massa grammoina
naulat_grammoina = naulat*32*13.3
luodit_grammoina = luodit*13.3

sum_grammoina = leiviskat_grammoina + naulat_grammoina + luodit_grammoina   #massa yhteensä grammoina

kilogram = int(sum_grammoina*0.001)    #kilogrammat kokonaislukuna, 1 g = 0,001 kg.
gram_jakojaannos = int(sum_grammoina%1000)  #jaetaan grammojen summa kilolla, saadaan jakojäännöksenä kokonais-
#luku "ylijäävistä" grammoista.

print(f"Massa nykymittojen mukaan on {kilogram} kilogrammaa ja {gram_jakojaannos} grammaa.")