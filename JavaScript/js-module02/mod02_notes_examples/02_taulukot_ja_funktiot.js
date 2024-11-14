"use strict";   // tällä voi välttää virheitä - ilmoittaa esim. jos on kaksi samannimistä muuttujaa

// array = taulukko
// function = funktio

console.log("moikkamoi");

// ARRAYS - taulukot ja taulukkorakenteet

// luodaan taulukko, hakasulkeet samoin kuin pythonissa
const items = [1,2,3,{name:"Ira"},[3,4,5],"merkkijono"];
console.log(items);   // konsolista voi tutkia taulukon rakennetta tarkemminn näyttää
                      // mitä kussakin alkiossa on; myös taulukon pituus on merkitty, nyt esim. 6.

// alkioon viitataan indeksillä:
console.log(items[0]);

// alkion arvoa voidaan muuttaa (tai lisätä alkioita) indeksin avulla:
items[0] = 99;
console.log(items);

// lisätään uusi indeksi (taulukon pituus on 6, joten pitää olla joku sen ulkopuolinen alkio)
// ei ole pakko olla seuraava vapaa indeksi, vaan niitä voi jättää tyhjäksi
items[9] = "Olen uusi jäsen" // nyt taulukon pituus on 10, vaikka on tyhjiä alkioita
console.log(items);

// välissä on nyt määrittelemätön arvo/alkio eli undefined
console.log(items[6]);

// taulukon pituuden voi tulostaa
console.log("Taulukon pituus:", items.length);  // ei tarvitse käyttää muotoilua `${}` vaan pilkulla voi erottaa
// tulostukset



// TAULUKOIDEN LÄPIKÄYNTI LOOPIN (SILMUKAN) AVULLA
console.log("------------------------------")

console.log("Perinteinen for-i-looppi:")
for (let i= 0; i < items.length; i++) {
  console.log(`${i+1}. jäsen (alkio ${i}): ${items[i]}`)
}

console.log("------------------------------")
// toinen looppi - for/in - ei käytetä juurikaan taulukoiden kanssa, vaan olioiden (joissa on avain)
console.log("Perinteinen looppi for/in -rakenteella, jolla saadaan avain/indeksi ja arvo")

for (const index in items) {
  console.log(index, items[index])
}

console.log("------------------------------")
// kolmas looppi - for/of - helppo ja nopea tapa iteroida läpi taulukko, jos indeksiä ei tarvita
console.log("Läpikäynti for/of-rakenteella, jolla saadaan arvot (tämä ei tulosta indeksiä):")

for (const item of items) {
  // if-lause, jossa tutkitaan onko alkio undefined
  if (typeof item !== "undefined") {
    console.log(item)

  // toinen tapa tehdä sama:
  //if (item !== undefined) {
  //  console.log(item)
    }
  //}
}

console.log("------------------------------")
// esimerkki materiaalista - luodaan taulukko ja tulostetaan jäsenet konsoliin
const names = ['Frank', 'Scott', 'Jasmine', 'Don'];
const ages = [23,28,32,101];
for (let i = 0; i < names.length; i++) {
  console.log(`Name: ${names[i]}`);
}


// TAULUKON METODIT (methods)
/*
- sort()            // sorts the array alphabetically = järjestää aakkosjärjestykseen
- reverse()         // reverses the items in the array in reverse order = laittaa käänteiseen järjestykseen
- shift()           // deletes and returns the 1st item in the array = poistaa ja palauttaa 1. jäsenen (eli 0. alkio)
- pop()             // deletes and returns the last item in the array = poistaa ja palauttaa viimeisen jäsenen
- push(value)       // adds the value at the end of the array, multiple values separated by commas = lisää arvon listan loppuun, samat arvot erotettu pilkulla
- includes(value)   // checks whether the array contains the given value = tarkistaa onko tietty arvo taulukossa, palauttaa true/false
- unshift()         // lisää taulukon alkuun alkion
*/

// järjestetään lista aakkosjärjestykseen:
names.sort();
console.log(names);

// vaihdetaan järjestys käänteiseksi
names.reverse();
console.log(names);

// ei toimi numeroiden kanssa sellaisenaan
// reverse, mutta luvuilla --> järjestää aakkosjärjestyksessä, eli nyt tulee väärä järjestys!
// tämä ei vertaa kokoa, vaan laittaa 101 ensimmäiseksi, koska 1 on ensimmäinen numero aakkosellisesti
ages.sort();
console.log(ages);

// tämä toimii numeroiden kanssa // numeroiden suuruusjärjestys, nouseva järjestys
ages.sort((a,b) => a - b);    // tässä notaatio: a on suurempi kuin b
console.log(ages);

// numerot suuruusjärjestykseen laskevassa järjestyksessä
ages.sort((a,b) => b - a);
console.log(ages);

// lisätään nimi taulukkoon
names.push("Ines");

// kun lisää jäsenen (tai muu toiminto), taulukko palauttaa samalla arvona TAULUKON PITUUDEN, voidaan ottaa se talteen muuttujaan
const newLength = names.push("Aku");
console.log(names);
console.log("Taulukon pituus:", newLength);

// lisätään alkio taulukon alkuun
names.unshift("Roope");
console.log(names);

// poistetaan taulukon viimeinen jäsen ja tallennetaan se muuttujaan
// eli taulukko palauttaa arvona poistetun jäsenen
const lastName = names.pop();
console.log("Poistettiin:", lastName);
console.log(names);

// poistetaan eka jäsen, tallennetaan muuttujaan
const firstName = names.shift();
console.log("Poistettiin:", firstName);
console.log(names);

// etsitään onko taulukossa ko. arvo, palauttaa true/false
console.log(names.includes("Scott"));   // palauttaa true/false suoraan konsoliin

//////////////////////////////
///////////////////////////////
console.log("---------------------------")
//////////////////////////////
//////////////////////////////

// OLIO (= object literal)
const duck = {
  name: "Tupu",
  age: "10",
}

// tulostetaan olio sellaisenaan, tyyppi = object
console.log(duck);

// tulostetaan olion tietty arvo avaimen avulla
console.log(duck["name"]);   // tässä pitää olla lainausmerkit, ei löydä vaikka oliossa se on ilman (eli ns. muuttujana)

// toinen tapa tulostaa olion arvo:
console.log(duck.age);

// muutetaan arvoja
duck.name = "Hupu Ankka";
duck.age = 12;
console.log(duck);

// lisätään uusia ominaisuuksia
duck.motto = "always ready";   // ammatti
console.log(duck);

console.log(`Hello, I am ${duck.name}, my age is ${duck.age} and my motto is "${duck.motto}".`);

// metodin luominen olioon ns. nimettömänä funktiona,
// olion sisälle voi tallentaa funktioita ja hakea tietty arvo

const duck2 = {
  name: "Ines",
  age: "32",
  getInfo: function() {
    return this.name + " is " + this.age + " years old.";      // funktioon viitataan this-sanalla, "tämän funktion arvo"
  }
}

// kutsutaan olion sisäistä funktiota
console.log(duck2.getInfo());

//////////////////////////////
///////////////////////////////
console.log("---------------------------")
//////////////////////////////
//////////////////////////////

// FUNKTIOT - 3 eri versiota / tyypillisintä tapaa kirjoittaa funktiot

/*
- ilman parametreja esim. greet();
- parametreilla
- nuolifunktio (kompakti tyyli rakentaa funktio, yksinkertainen/lyhyt)

 */

// perinteinen funktiomäärittely, jossa on yksi parametri
function greet(name) {
 console.log(`Hello, ${name}!`)
}

// funktion ilmaisu = function expression = anonyymi (ei nimeä) funktio, joka tallennetaan muuttujaan
const greet2 = function(name) {
 console.log(`Hello again, ${name}!`)
}

// nuolifunktio = arrow function // "kun kutsut muuttujaa, suorita seuraava (nimetön) funktio"
const greet3 = (name) => {
  console.log(`Hello third time, ${name}!!!`)
}

// kutsutaan kaikkia kolmea luotua funktiota
greet("Hagrid");
greet2("Hagrid");
greet3("Hagrid");

//////////////////////////////
///////////////////////////////
console.log("---------------------------")
//////////////////////////////
//////////////////////////////

// tuntiesimerkki 2.2
// Write a program that asks the user for the number of participants. After this, the program
// asks for the names of all participants. Finally, the program prints the names of the
// participants on the web page in an ordered list (<ol>) in alphabetical order. (2p)
console.log("Assignment 2.2")
const participantNames = [];
let participantsHTML = "";

// HTML-dokumentista voi hakea tietoa, esim. jos HTML:ssä on lista:
const namelist = document.querySelector("#namelist");
// kun etsii jotakin elementtiä, kannattaa tulostaa se konsoliin (näkee toimiiko, testi)
console.log(namelist);
namelist.innerHTML = "";

// kysytään osallistujamäärä
const num = parseInt(prompt("Give a number of participants."));

// luodaan funktio, joka kysyy nimet
function askNames() {
  for (let i = 0; i < num; i++) {
    console.log(i);
    let name = prompt("Enter a name.");
    participantNames.push(name);
  }

  console.log(participantNames);

}

// lisätään taulukon jäsenet HTML-dokumenttiin
function printNames() {
  // versio 1. käytetään for/i-looppia ja innerHTML (for/i-loopin käyttö silloin, kun tarvitsee iteraattorin)
  //for (let i = 0; i < participantNames.length; i++) {
  //  // tulostetaan nimet konsoliin
  //  console.log(participantNames[i]);
  //  participantsHTML += `<li>${participantNames[i]}</li>`
  //}
  //namelist.innerHTML = participantsHTML;
  //console.log(participantsHTML);

  // PAREMPI TAPA LUODA <li>-elementit: DOM // !!!!!!!!!!!!!!!!!!!!!!!!!
  // versio 2. for/of ja create element // jos haluaa käydä taulukon kaikki arvot läpi (ilman indeksiä), voi käyttää for/of-silmukkaa
  for (const name of participantNames) {
    console.log(name);

    // luodaan tyhjä elementti <li></li>
    let liElement = document.createElement('li');

    // annetaan elementille sisältö <li>name</li>
    liElement.innerHTML = name;

    // lisätään HTML-dokumentissa olevalle <ol>-elementille lapsielementti <li> eli loopissa aina uusi rivi
    namelist.appendChild(liElement);
  }
}

// kutsutaan funktioita
askNames();
printNames();
