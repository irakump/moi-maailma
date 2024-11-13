// Assignment 2.4
// Write a program that asks the user for numbers until they give zero. The given
// numbers are printed in the console from the largest to the smallest. (2p)

"use strict";

const numbers = [];
let number = 1;

// pyydetään numeroita, kunnes käyttäjä syöttää nollan
while (number !== 0) {
  number = parseInt(prompt("Enter a number."));
  numbers.push(number);
}

// järjestetään numerot suuruusjärjestykseen, laskeva järjestys
numbers.sort((a,b) => (b - a));

// tulostetaan numerot konsoliin
for (let n in numbers) {
  console.log(numbers[n]);
}
