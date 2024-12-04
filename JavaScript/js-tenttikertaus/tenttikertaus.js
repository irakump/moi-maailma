// mod01 vuorovaikutteiset ohjelmat

// js on yleistä käyttää heittomerkkejä '' (lainausmerkkien sijasta)

const age = 21;
const ageStr = age.toString();   // funktio toString() muuttaa luvun merkkijonoksi
console.log(typeof ageStr);             // konsoliin tulostuu 'string'

var name = 'Anneli';              // var- ja let-muuttujien arvoa voi vaihtaa, const ei.
console.log(`Name is ${name}.`);        // `` -merkeillä ja ${} voi sisällyttää muuttujia tulosteeseen
name = 'Pirjo';
console.log('...');
console.log(`Name has changed to ${name}.`)

// html:n defer scriptin sisällä: käy läpi koko HTML-dokumentin, ja vasta sen jälkeen
// lisää javascriptin ominaisuudet

// alert() -funktio tulostaa ikkunaan tekstin, käyttäjä kuittaa painamalla OK
//alert('This is an alert!');

// muuttujien (variable) tyypit
/*
-boolean = true, false
-numero = numeric: int, float
-string
-null (tyhjä arvo)
-undefined = ei määritetty, eli tyyppiä ei tiedetä = tuntematon
-symbol
 */

// merkkijonon muuttaminen numeroksi
const ageString = '44';
const ageInt = parseInt(ageString);
console.log('....................')
console.log(typeof ageInt);
const moneyStr= '15.48';
const money = parseFloat(moneyStr);
console.log(`Type of ${money} is ${typeof money}.`);

console.log('....................')

// muutoksen stringistä numeroksi voi tehdä myös plussalla +  :
const money2 = '22.11';
console.log(typeof money2);
const money1 = +money2;
console.log(typeof money1);

console.log('....................')

// prompt() -funktioon voi antaa syötteen
//const userName = prompt('Enter name.');
//console.log(`User's name is ${userName}.`);

// matemaattiset operaatiot
/*
summa = summation +
vähennys = subtraction -
kerto = multiplication *
jako = division /
jakojäännös = modulo % (esim 3%2===1, laskee kokonaisluvuilla jakojäännöksen. 7%5===2)

 */
console.log(3%2);

// ++ kasvattaa lukua yhdellä
// -- vähentyy yhdellä
// number += 5    --> lukuun lisätään 5, toimii myös muilla operaatioilla samoin

// Math-object:
// voi laskea neliöjuuren tai saada random-luvun väliltä 0..1
console.log(Math.sqrt(3));  // neliöjuuri Math.sqrt(num);
console.log(Math.random());   // arvotaan luku

'use strict';       // tämä varmistaa, että ohjelma on 'strict modessa', jolloin error-viesti tulostuu
// esim. jos yrittää määritellä muuttujaa ilman let tai const -määrittelijää

///////////////////////////////////////////////////
// valinta-toistorakenteet = conditional expressions

// looginen ilmaisu (logical expression) = true tai false
// esim.
const age3 = 15;
if (age < 18) {       // true, koska 15 < 18
  console.log('You are a minor.');
}

// jos ehto on epätosi, ei sitä suoriteta

// vertailuoperaattorit = comparison operators
// equal to == tai ===    // === myös tyyppi on sama, esim. 7 == '7' on true, mutta 7 === '7' false
// != eri kuin
// < pienempi kuin
// > suurempi kuin
// >= suurempi tai yhtä suuri kuin

// loogiset operaattorit: negaatio, ja, tai
/*
! negaatio: tulee reverse eli vastakohta ehdolle.
&& ja: molempien tulee olla totta. esim. if (2-1===1 && 1 < 2) = true
|| tai: jompi kumpi tai molemmat ovat totta

*/

// loopit = toistorakenteet (3 vaihtoehtoa: while, do/while, for)


// Math.random() pystyy tekemään nopan (do/while):
let result;
do {
   result = Math.floor(Math.random()*6)+1;
    console.log(result);
} while (result < 6);

// Math.floor() -funktio pyöristää luvun alaspäin kokonaislukuun, esim. Math.floor(5.95) === 5
// noppa: kertoo luvun väliltä 0..1 kuudella ja lisää yhden - saadaan luvut 1-6
// yllä oleva noppa: heitetään, kunnes saadaan tulos 6

// for/i -looppi: iteraattori kasvaa, looppi pyörii kunnes ylittää ehdon
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
// yllä oleva tulostaa konsoliin luvut 1-10

//////////////////////////////////////////////////

// moduuli 2
// array = taulukko
const array = ["Aino", "Hai", "Baabel", "Arja"];
array.sort(); // järjestää aakkosjärjestykseen
console.log(array);
const numbers = [0, 90, 4, 1]
numbers.sort((a,b) => a-b); // järjestää numerot suuruusjärjestykseen
console.log(numbers);

// moduuli 3 - BOM = browser object model
// confirm() avaa pop-up-ikkunan jossa on teksti ja kaksi nappia: OK, Cancel
//  OK===true, Cancel===false   // nämä palautuu

// prompt() avaa pop-upin, johon voi kirjoittaa
//prompt('Otsikko', 'tässä tekstiä alkuun');
// jos kenttä on tyhjä, palautuu arvo null

// node = solmu, jokainen elementti, attribuutti ja konteksti (esim. teksti) on node

// mod4
