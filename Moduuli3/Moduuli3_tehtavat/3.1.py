# Tehtävä 3.1:
# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha_lenght = float(input("Kerro kuhan pituus (cm): "))     #kysytään kuhan pituus

alamittainen_kuha = kuha_lenght < 37        #luodaan muuttuja, alamittainen kuha

if alamittainen_kuha:   #jos ehto on tosi, tulostuu rivin 9 teksti
    print(f"Kuha on alamittainen, laske se takaisin järveen. Alimmasta sallitusta pyyntimitasta (37 cm) puuttuu {37 - kuha_lenght} cm.")
else:                   #jos ehto on epätosi, tulostuu rivin 11 teksti
    print(f"Kuhan pituus ylittää alimman sallitun pyyntimitan (37 cm), voit pitää sen.")
