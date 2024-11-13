// Assignment 2.1
// Write a program that prompts the user for five numbers and prints them in the reverse
// order they were entered. Print the result to the console. (2p)
// Save the numbers to an array, then use for-loop to iterate in reverse order.
// Do not use array.reverse() function.

"use strict";

// luodaan tyhjä taulukko
const numbers = [];

// pyydetään numerot ja lisätään taulukon loppuun
for (let i = 0; i < 5; i++) {
  const num = parseInt(prompt(`Enter ${i+1}. number.`));
  numbers.push(num);
}

console.log("Taulukko:", numbers);

// tallennetaan listan pituus muuttujaan
let numbersLength = numbers.length;

// tulostetaan numerot käänteisessä järjestyksessä
for (let i = 0; i < numbersLength; i++) {
  // poistetaan taulukon viimeinen numero, tallennetaan muuttujaan ja tulostetaan
  const lastNum = numbers.pop();
  console.log(lastNum);
}
