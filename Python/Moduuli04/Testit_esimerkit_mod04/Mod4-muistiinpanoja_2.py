# while-rakenteeseen voidaan lisätä else-haara: suoritetaan onnistuneen while-rakenteen päätteeksi
# jos on break-komento ennen sitä, else-haaraa ei suoriteta.

#esim6. - else-haara break-rakenteessa:

komento = input ("Anna komento: ")
while komento!="lopeta":
    if komento=="MAYDAY":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print ("Näkemiin.")
print ("Toiminnot lopetettu.")

"""
IKUINEN SILMUKKA = virhe
-käy esim. silloin, jos toistorakeenteen sisällä ei kasvata muuttujan arvoa, 
jolloin while-ehto ei muutu koskaan epätodeksi
"""

"""
Python-kielessä on kuusi muuttujan perustyyppiä:

-merkkijono (string)
-luku (number), joka voi olla kokonaisluku, pitkä kokonaisluku, liukuluku tai kompleksiluku
-totuusarvo (boolean), joka voi olla True tai False
-lista (list)
-monikko (tuple)
-sanakirja (dictionary)

"""