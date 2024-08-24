# Tehtävä 2.5
# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa, yksi naula 32 luotia ja yksi luoti 13,3 grammaa.

print("Kerro massa keskiaikaisten mittojen mukaan.")
leiviskat = float(input("Anna leiviskät: "))    #float - merkkijonosta tulee suoraan liukuluku
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leiviskat_grammoina = leiviskat*20*32*13.3  #lasketaan massa grammoina
naulat_grammoina = naulat*32*13.3
luodit_grammoina = luodit*13.3

sum_grammoina = leiviskat_grammoina + naulat_grammoina + luodit_grammoina   #massa yhteensä grammoina
print(sum_grammoina)

kilogram_tasaluku = int(sum_grammoina*0.001)    #kilogrammat kokonaislukuna

print(f"Massa on {kilogram_tasaluku} kilogrammaa")

grammat_tasaluku = int(sum_grammoina - (kilogram_tasaluku*1000))  #1 kg = 1000 g. Grammat kokonaislukuna, vähennetään kilogrammojen osuus (grammoina)

print(f"Massa nykymittojen mukaan on {kilogram_tasaluku} kilogrammaa ja {grammat_tasaluku} grammaa.")

#Kokeile tehdä myös jakojäännöksen kautta? grammat_tasa = int(sum_grammoina%(kilogram_tasaluku*1000)) - jäljelle jää grammojen osuus?

#grammat_tasa = int(sum_grammoina%(kilogram_tasaluku*1000))  #toimii
#print(grammat_tasa)
