# Tehtävä 2.5
# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa:   leiviskat*20*32*13.3 (grammaa)  #leiviskät grammoina
# Yksi naula on 32 luotia:      naulat*32*13.3 (grammaa)    #naulat grammoina
# Yksi luoti on 13,3 grammaa:   luodit*13.3 (grammaa)   #luodit grammoina

print("Kerro massa keskiaikaisten mittojen mukaan.")
leiviskat = input("Anna leiviskät: ")
naulat = input("Anna naulat: ")
luodit = input("Anna luodit: ")

leiviskat_grammoina = float(leiviskat)*20*32*13.3
naulat_grammoina = float(naulat)*32*13.3
luodit_grammoina = float(luodit)*13.3

sum_grammoina = float(leiviskat_grammoina) + float(naulat_grammoina) + float(luodit_grammoina)  #summa grammoina

grams_to_kilograms = (sum_grammoina)*0.001   #grammojen muutos kilogrammoiksi, 1 g = 0,001 kg ( = 1/1000 kg)

#koko massa on sum_grammoina.
#sum_gram_minus_sum_kilogram =        #kokonaismassasta vähennetään kilogrammat

print(f"Massa on {grams_to_kilograms:.0f} kilogrammaa")   #kilogrammat kokonaislukuna

#miten rivi 25 saisi grams_to_kilograms:.0f muuttujaksi? Sen voisi muuttaa taas grammoiksi ja vähentää koko massasta.

#print(f{grams_to_kilograms:.0f})

#kilogrammojen (kokonaisluku) muutos takaisin grammoiksi:
#kg_to_g = grams_to_kilograms:.0f

print(" ")
print(f"Massa on {sum_grammoina:.1f} grammaa.")     #tulostuu kokonaisluku (.0f), pyöristääkö vai jättääkö desim. pois?


#puuttuu vielä kilogrammat, ja siitä jakojäännös. Vastauksen tulee olla "Massa on x kilogrammaa ja y grammaa.

#Onko mahdollista näin vai pitääkö käyttää jakojäännöstä % tai toinen juttu // ???

print("Massa nykymittojen mukaan on ")
