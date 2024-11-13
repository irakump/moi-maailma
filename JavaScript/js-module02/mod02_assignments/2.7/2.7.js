// Assignment 2.7
// Modify the function above so that it gets the number of sides on the dice as a parameter.
// With the modified function you can for example roll a 21-sided role-playing dice. The
// difference to the last exercise is that the dice rolling in the main program continues
// until the program gets the maximum number on the dice, which is asked from the user at
// the beginning. (2p)

"use strict";

const diceSides = parseInt(prompt("Enter the number of sides of the dice."));

// luodaan funktio
function rollADice(diceSides) {
  let diceRoll = Math.floor(Math.random() * diceSides) + 1;
  return diceRoll;
}

// pääohjelma

let diceResult = 0;
let diceResultHTML = "";

// heitetään noppaa, kunnes saadaan nopan suurin luku
while (diceResult !== diceSides) {
  diceResult = rollADice(diceSides);
  diceResultHTML += `<li>${diceResult}</li>`;
}

document.querySelector("#text").innerHTML = `Let's roll a dice until the result is ${diceSides}.`;
document.querySelector("#result").innerHTML = diceResultHTML;
