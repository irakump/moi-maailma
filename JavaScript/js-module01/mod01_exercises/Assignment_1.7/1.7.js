// Assignment 1.7
// Write a program that rolls user defined number of dice and displays the sum of
// the results of the dice rolls. (2p)

// First, program asks the user for the number of dice rolls.
// Then the program throws a die as many times as the user defined.
// Print the sum of the results in the console or in the HTML document.
//
"use strict";

const diceTotal = parseInt(prompt("How many dice should I roll? Enter a number."));
let sum = 0;

let diceThrown = 0;

while (diceThrown < diceTotal) {
  // arvotaan luku väliltä ]0, 1[
  let diceResult = Math.random();
  // muutetaan luku nopan silmäluvuiksi [1, 6]
  if (diceResult < (1 / 6)) {
    diceResult = 1;
  } else if (diceResult < (2 / 6)) {
    diceResult = 2;
  } else if (diceResult < (3 / 6)) {
    diceResult = 3;
  } else if (diceResult < (4 / 6)) {
    diceResult = 4;
  } else if (diceResult < (5 / 6)) {
    diceResult = 5;
  } else {
    diceResult = 6;
  }
  console.log(`Dice result: ${diceResult}`);
  sum += diceResult;     // lisätään noppa summaan
  diceThrown++;         // kasvatetaan muuttujaa yhdellä
}

// tulostetaan tulos HTML-dokumenttiin ja konsoliin
document.querySelector("#result").innerHTML = `Dice rolled: ${diceTotal}, sum: ${sum}`;
console.log(`Sum: ${sum}`);
