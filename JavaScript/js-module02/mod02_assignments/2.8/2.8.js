// Assignment 2.8
// Write a function called concat(), which receives an array of strings as a parameter.
// The function returns a string formed by concatenating the elements of the array. (2p)
// Example: In a four-item array, there are items Johnny, DeeDee, Joey and Marky. The
// function returns the string JohnnyDeeDeeJoeyMarky.
// Do not use array.join() function
// You can hardcode the array, no need for prompt().
// Print the result to HTML document.

"use strict";

// luodaan taulukko
const names = ["Harry", "Hermione", "Ron", "Dumbledore", "Voldemort"];


// luodaan funktio, joka palauttaa taulukon alkiot ketjuna
function concat(array) {
  let concatenation = "";
  for (const n in array) {
    concatenation += array[n];
  }
  return concatenation
}

document.querySelector("#result").innerHTML = concat(names);
