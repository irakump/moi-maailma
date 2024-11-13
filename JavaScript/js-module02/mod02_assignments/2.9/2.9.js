// Assignment 2.9
// Write a function called even(), which receives an array containing numbers as a parameter.
// The function returns a second (usually smaller) array which has the even numbers of the
// original array. The function must not make changes to the original table. (3p)
// Example: In a three-item array, there are items 2, 7 and 4. The function returns a two-item
// array with items 2 and 4.
// Print both the original array and the new array to the console in the main program after
// you have called the function.
// You can hard code the array, no need for prompt().

"use strict";

const numbers = [1, 6, 9, 10, 3, 4, 2];
const evenNumbers = [];

// luodaan funktio, joka palauttaa syötetystä taulukosta parillisten numeroiden taulukon
function even(array) {
  // käydään taulukko läpi ja tallennetaan parilliset luvut toiseen listaan
  for (const a in array) {
    if (array[a] % 2 === 0) {
      evenNumbers.push(array[a]);
    }
  }
}

// pääohjelma
even(numbers);
console.log("Original list:", numbers);
console.log("New list:", evenNumbers);
