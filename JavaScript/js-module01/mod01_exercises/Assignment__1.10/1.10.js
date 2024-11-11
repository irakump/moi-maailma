// Assignment 1.10
// Make a program that asks the user for the number of dice and the sum of the eye numbers of
// interest to the user. The purpose of your program is now to find out with what probability
// the number of dice given by the user produces the sum of the number of eyes given by the user.
// For example, if the user enters 3 as the number of dice and 17 as the sum of the eyes, the
// program calculates the probability that the sum of the three dice's eye numbers is 17. (5p)

// Solve the problem by simulating: Have the program roll a given number of dice in a for-loop
// (e.g. 10,000 times) and calculate what proportion of the repetitions produced the sum of eye
// numbers of interest to the user.

// Print the result on the HTML document:
// Probability to get sum 7 with 2 dice is 15.64%
// you can limit the number of decimals with toFixed()
// test values:
// 2 dice, sum 7, probability is about 15-17%
// 3 dice, sum 15, probability is about 5%

"use strict";

const diceTotal = parseInt(prompt("Enter the number of dice."));
const sumNumbers = parseInt(prompt("Enter the sum of eye numbers."));

let sumNumbersTotal = 0, diceThrownTotal = 0;

// noppasetin heitto 10 000 kertaa
while (diceThrownTotal < 10000) {
  // noppien heitto käyttäjän syöttämän määrän mukaan = noppasetti
  let sum = 0, diceThrown = 0;

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
    //console.log(`Dice result: ${diceResult}`);
    sum += diceResult;                         // lisätään noppa summaan
    diceThrown++;                             // kasvatetaan muuttujaa yhdellä
  }

  // kasvatetaan muuttujaa, jos noppien summa on sama kuin käyttäjän syöttämä summa
  if (sum === sumNumbers) {
    sumNumbersTotal++;
  }
  diceThrownTotal++;
}

// lasketaan (halutun summan) todennäköisyys
const probability = (sumNumbersTotal / diceThrownTotal) * 100;
const p = probability.toFixed(2);  // todennäköisyys 2 desimaalin tarkkuudella

// tulostetaan tulokset konsoliin ja HTML-dokumenttiin
console.log(`Correct sum rolled: ${sumNumbersTotal} times`);
console.log(`Probability: ${p} %`);

document.querySelector("#probability").innerHTML = `Probability to get sum ${sumNumbers} 
with ${diceTotal} dice is ${p} %`;
