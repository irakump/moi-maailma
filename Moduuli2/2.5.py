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

leiviskat_grammoina = float(leiviskat)*20*32*13.3   #ei kannata olla float ja laskutoimitus samassa, ennemmin erikseen selkeyden vuoksi. esim. leiviskat_grammoina = float(leiviskat) ja seuraava rivi olisi lasku.
                                                    #voi myös laittaa float jo 10.-12. riveille: leiviskat = float(input("Anna leiviskät: "), jolloin muuttuja on heti numero, eikä tarvitse erikseen muuttaa luvuksi.

naulat_grammoina = float(naulat)*32*13.3
luodit_grammoina = float(luodit)*13.3

sum_grammoina = float(leiviskat_grammoina) + float(naulat_grammoina) + float(luodit_grammoina)  #summa grammoina

kilogram = sum_grammoina*0.001   #grammojen muutos kilogrammoiksi, 1 g = 0,001 kg ( = 1/1000 kg) #jos ei toimi, pitääkö käyttää float eli muuttaa luvuksi?

tasaluku_kilogram = int(kilogram)   #tämä antaa tasaluvun, int = tasaluku. #int voisi laittaa myös suoraan riville 20? esim. kilogram = int(sum_grammoina*0.001) #nimeä silloin rivi 20 tasaluku_kilogram.

#koko massa on sum_grammoina.
#kokonaismassasta vähennetään kilogrammat (rivi 29)

print(f"Massa on {tasaluku_kilogram} kilogrammaa")   #kilogrammat kokonaislukuna

grammat_jakojaannos_tasaluku = int(sum_grammoina - (tasaluku_kilogram*1000))  #1 kg = 1000 g. Tässä tulee grammojen osuus eli jakojäännös kokonaislukuna.

print(f"Massa nykymittojen mukaan on {tasaluku_kilogram} kilogrammaa ja {grammat_jakojaannos_tasaluku} grammaa.")

#Onko mahdollista näin vai pitääkö käyttää jakojäännöstä % tai toinen juttu // ???
