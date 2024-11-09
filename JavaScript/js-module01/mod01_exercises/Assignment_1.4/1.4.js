// Assignment 1.4
// In the Harry Potter children's books, the sorting hat assigns a new student at Hogwarts School
// of Witchcraft and Wizardry to one of the four classes, which are Gryffindor, Slytherin, Hufflepuff,
// and Ravenclaw. Write an electronic sorting hat that asks for a student's name and draws a room for
// them. If you enter Anna as the name, for example, the program prints to the HTML document "Anna, you
// are Ravenclaw." (3p)

// Use math.random() to draw a value (1, 2, 3 or 4)
// Once the number is drawn, you need to use a multiple choice structure
// (if, else if, ..., else or switch).

"use strict";

// pyydetään nimi
const name = prompt("Write your name.");

// lajitteluhattu arpoo numeron väliltä ]0, 1[ - muutetaan arvo ja valitaan tupa
let num = parseFloat(Math.random());
let room;

if (num <= 0.25) {
  num = 1;
  room = "Gryffindor";
} else if (num <= 0.5) {
  num = 2;
  room = "Slytherin";
} else if (num <= 0.75) {
  num = 3;
  room = "Hufflepuff";
} else if (num > 0.75) {
  num = 4;
  room = "Ravenclaw";
}

console.log("Drawn value:", num);
document.querySelector("#target").innerHTML = `${name}, you are ${room}.`;
