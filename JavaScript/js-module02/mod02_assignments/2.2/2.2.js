// Assignment 2.2
// Write a program that asks the user for the number of participants. After this, the program
// asks for the names of all participants. Finally, the program prints the names of the
// participants on the web page in an ordered list (<ol>) in alphabetical order. (2p)

"use strict";

// pyydetään numero
const partNum = parseInt(prompt("Enter the numer of participants."));
const names = [];

// pyydetään nimet, tallennetaan taulukkoon
for (let i = 1; i <= partNum; i++) {
  let name = prompt(`Enter the name of ${i}. participant.`);
  names.push(name);
}

// järjestetään taulukko aakkosjärjestykseen
names.sort();

// luodaan muuttuja nimiä varten
let namesHTML = "";

// tallennetaan kaikki nimet yhteen muuttujaan merkkijonoksi
for (let n in names) {
  namesHTML += `<li>${names[n]}</li>`
}

// tulostukset
document.querySelector("#header").innerHTML = "Participants in alphabetical order";
document.querySelector("#names").innerHTML = namesHTML;
