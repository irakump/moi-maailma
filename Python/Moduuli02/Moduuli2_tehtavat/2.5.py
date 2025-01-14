# Tehtävä 2.5
# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
# Yksi leiviskä on 20 naulaa, yksi naula 32 luotia ja yksi luoti 13,3 grammaa.

print("Kerro massa keskiaikaisten mittojen mukaan.")
leiviskat = float(input("Anna leiviskät: "))    #kysytään leiviskät
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leiviskat_gram = leiviskat*20*32*13.3  #lasketaan leivisköjen massa grammoina
naulat_gram = naulat*32*13.3
luodit_gram = luodit*13.3

sum_gram = leiviskat_gram + naulat_gram + luodit_gram   #lasketaan massa yhteensä grammoina

kilogram = int(sum_gram*0.001)    #muutetaan grammat kilogrammoiksi (kokonaisluku). 1 g = 0,001 kg.
gram_jakojaannos = int(sum_gram%1000)  #grammojen jakojäännös kokonaislukuna

print(f"Massa nykymittojen mukaan on {kilogram} kilogrammaa ja {gram_jakojaannos} grammaa.")
