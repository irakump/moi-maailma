// Assignment 2.3
// Write a program that asks for the names of six dogs. The program prints dog names
// to unordered list <ul> in reverse alphabetical order. (2p)

"use strict";

let dogs = [];

// pyydetään koirien nimet ja tallennetaan taulukkoon
for (let i = 1; i <= 6; i++) {
  let dogName = prompt(`Enter ${i}. dog name.`);
  dogs.push(dogName);
}

// järjestetään lista aakkosjärjestykseen
dogs.sort();
// käänteinen järjestys
dogs.reverse();

// muuttuja koiria varten
let dogsHTML = "";

// lisätään koirien nimet muuttujaan lista-elementeissä
for (let dog in dogs) {
  dogsHTML += `<li>${dogs[dog]}</li>`;
}

// tulostukset
document.querySelector("#header").innerHTML = "Dogs in reverse alphabetical order";
document.querySelector("#dogs").innerHTML = dogsHTML;
