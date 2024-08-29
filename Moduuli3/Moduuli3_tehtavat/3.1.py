"""
Tehtävä 3.1
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""

kuha_lenght = float(input("Kerro kuhan pituus (cm): "))     #kysytään kuhan pituus

if (kuha_lenght < 37):                      #ehto on tosi, kun kuha on alamittainen
    print(f"Kuha on alamittainen, laske se takaisin järveen. Alimmasta sallitusta pyyntimitasta (37 cm) puuttuu {37 - kuha_lenght:.2f} cm.")            #rajataan desimaalit kahteen
else:
    print(f"Kuhan pituus ylittää alimman sallitun pyyntimitan (37 cm), voit pitää sen.")
