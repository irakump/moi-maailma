// Assignment 2.5
// Write a program that prompts the user for numbers. When the user enters one of the
// numbers he previously entered, the program will announce that the number has already
// been given and stops its operation and then prints all the given numbers to the console
// in ascending order. (2p)

"use strict";

let numberGiven = false;
const numbers = [];

while (numberGiven === false) {
  const number = parseInt(prompt("Enter a number."));
  // tarkistetaan, onko numero taulukossa
  if (numbers.includes(number)) {
    numberGiven = true;
    alert("The number has already been given.")
  } else {
    // jos numero ei ole taulukossa, lisätään se
    numbers.push(number);
  }
}

// järjestetään lista nousevaan järjestykseen ja tulostetaan
numbers.sort((a,b) => a - b);
for (let n in numbers) {
  console.log(numbers[n])
}
