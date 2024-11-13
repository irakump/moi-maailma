// Assignment 2.6
// Write a function that returns a random dice roll between 1 and 6. The function should
// not have any parameters. Write a main program that rolls the dice until the result is 6.
// The main program should print out the result of each roll in an unordered list (<ul>). (2p)

"use strict";

// luodaan funktio
function rollADice() {
  let diceRoll = Math.random();
  // muutetaan arvottu luku nopan silmäluvuksi [1, 6]
  if (diceRoll < 1 / 6) {
    diceRoll = 1;
  } else if (diceRoll < 2 / 6) {
    diceRoll = 2;
  } else if (diceRoll < 3 / 6) {
    diceRoll = 3;
  } else if (diceRoll < 4 / 6) {
    diceRoll = 4;
  } else if (diceRoll < 5 / 6) {
    diceRoll = 5;
  } else {
    diceRoll = 6;
  }
  return diceRoll;
}

// pääohjelma

// määritetään muuttujat
let diceResult = 0;
let diceResultHTML = "";

// kutsutaan funktiota, kunnes saadaan luku 6
while (diceResult !== 6) {
  diceResult = rollADice();
  diceResultHTML += `<li>${diceResult}</li>`;
}
document.querySelector("#text").innerHTML = "Let's roll a dice until the result is 6."
document.querySelector("#result").innerHTML = diceResultHTML;
