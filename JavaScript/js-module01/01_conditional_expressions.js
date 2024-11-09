'use strict';
console.log('Moikka maailma 1234');

// kommentit kahdella kautta-viivalla, moniriviset kommentit /* */

/* if-lauseissa (ehtolause) totuusarvo tulee aina sulkuihin ja lopuksi
 aaltosulkeet, tapahtuva asia tulee aaltosulkeiden sisään, esim. if (true) {console.log("true")}
 -ehdon täytyy olla aina true tai false (javascriptissä molemmat pienellä alkukirjaimella, vs. pythonissa on True ja False)

-JavaScriptissä kaksiosaiset muuttujan nimet kirjoitetaan yhteen: randomNumber, ei random_number
    alaviivaa käytetään vain pythonissa

 -ja = &&    tai = ||    --> toimii samoin kuin pythonissa and, or
*/

// muuttujat: ensisijaisesti luodaan const:n avulla (muuttumaton), mutta jos on tarvetta
// muokata sitä, käytetään let (esim. pyydetään promptilla (input) käyttäjää syöttämään ikä)

// arvotaan testinumero
const randomNumber = Math.random();   // palauttaa jonkun numeron väliltä ]0, 1[(liukuluku = float)
// jos haluaa arpoa suuremmalta väliltä, pitää laskea. esim. Math.random() * 10
// jos haluaa kokonaisluvun, voi pyöristää desimaaleja pois

// testaaminen, jos kolikko jää kyljelleen: kovakoodaa numero
//const randomNumber = 0.503

console.log('arvottu numero', randomNumber);   // tulosteet erotetaan pilkulla

// esim 1. - kolikon heitto
// 49,9 % todennäköisyys saada kruuna tai klaava (kolikko voi jäädä pystyyn)
if (randomNumber < 0.495) {
  console.log('kruuna');
} else if (randomNumber > 0.505) {
  console.log('klaava');
} else {
  console.log('kolikko jää kantilleen');
}

// aaltosulkeen jälkeen jatkuu ohjelman suoritus
console.log('Ohjelman suoritus jatkuu ehtolauseen jälkeen');

/*
VERTAILUOPERAATTORIT:
- yhtä suuri kuin == (ei vertaa tyyppiä eli 1 == "1" on true)
              TAI === (vertaa muuttujan tyyppiä eli 1 === "1" = false)

--> muuten samat kuin pythonissa:
- eri suuri kuin !=     tai !==
- suurempi kuin >
- suurempi tai yhtä suuri kuin >=
- pienempi kuin <
- pienempi tai yhtä suuri kuin <=
 */

/*
LOOGISET OPERAATTORIT:
- ja: &&
- negaatio (ei): !        // esim. pythonissa not true on js:ssä !true
- tai: ||
 */

// esim2. switch - pystyy tekemään saman kuin else if -lauseilla JA voi yhdistää
// ehtoja (ja, tai, ..). Switcillä voi käsitellä esim. erilaisia valikkoja

/*
const cabinClass = prompt("Enter the cabin class (A/B/C).");
switch (cabinClass) {
    case 'A':
        console.log('Top deck cabin with window.');
        break;
    case 'B':
        console.log('Top deck cabin without window.');
        break;
    case 'C':
        console.log('Windowless cabin under the car deck.');
        break;
    default:
        console.log("Invalid cabin class.");
}
*/

//  toistorakenteet = silmukat = loopit

console.log('arvottu numero', randomNumber);   // tulosteet erotetaan pilkulla
// esim3. - kuinka monta heittoa menee, että kolikko jää kyljelleen? (49,9 % todnäk. kruuna/klaava)

let throwCount = 0;
let stillThrowing = true;
while (stillThrowing) {
  const randomNumber = Math.random();    // tämä on muuttumaton, eli silmukka ei arvo lukua uudelleen
  throwCount++;
  if (randomNumber < 0.495) {
    console.log('kruuna');
  } else if (randomNumber > 0.505) {
    console.log('klaava');
  } else {
    console.log('kolikko jää kantilleen');
    console.log('heittojen lkm', throwCount);
    stillThrowing = false;
  }
}

// puolipiste lauseen jälkeen ei ole pakollinen javascriptissä, mutta kannattaa käyttää selkeyden vuoksi, ei ole
// pakollista. Puolipiste ; päättää lauseen. Koodi toimii myös ilman niitä (on muutamia poikkeuksia, joissa on
// pakko käyttää?) ---> jompi kumpi: joko puolipisteet aina tai ei koskaan

// do/while - ehto testataan silmukan jälkeen (tätä harvemmin käytetään oikeissa töissä)

// yksinkertainen for-silmukka (yleisempi kuin do/while-silmukka)
for (let i = 1; i < 10; i *= 2) {     // ehto on suluissa. Ensin esitellään muuttuja, sitten puolipiste,
  console.log("iin arvo:", i);                           // seuraavaksi ehto: "kuinka kauan ajetaan", tässä niin kauan kun i on pienempi kuin 1
}

// arvojen kasvattaminen: i++ (tämä lisää lukuun i luvun 1)
//                        i += 2 (voi määritellä, mikä luku lisätään
// arvojen vähentäminen: i -= 1

// esim. - kuinka monta heittoa menee keskimäärin, että kolikko jää kantilleen (monimutkaisempi for-silmukka)
const throwCounts = [];         // js:ssä tämä on tyhjä taulukko (ei lista)

for (let i=0; i < 100; i++) {

    let throwCount = 0;
    let stillThrowing = true;

    while (stillThrowing) {
      const randomNumber = Math.random();    // tämä on muuttumaton, eli silmukka ei arvo lukua uudelleen
      throwCount++;
      if (randomNumber < 0.495) {
        console.log("kruuna");
      } else if (randomNumber > 0.505) {
        console.log("klaava");
      } else {
        console.log("kolikko jää kantilleen");
        console.log("heittojen lkm", throwCount);
        throwCounts.push(throwCount);       // push vastaa samaa kuin pythonin append (lisää alkion listaan)
        stillThrowing = false;
      }
    }
}
console.log("heittojen lukumäärät: ", throwCounts)

// lasketaan heittomäärien keskiarvo for-silmukalla
let sum = 0;
for (let i=0; i<throwCounts.length; i++) {
    sum += throwCounts[i]    // sama kuin sum = sum + throwCounts
}
//console.log(throwCounts.length)
console.log("heittojen keskiarvo: ", sum/throwCounts.length)

