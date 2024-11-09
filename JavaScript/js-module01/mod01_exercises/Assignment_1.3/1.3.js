// Assignment 1.3
// Write a program that prompts for three integers. The program prints the sum,
// product and average of the numbers to the HTML document. (3p)

"use strict";

// pyydetään käyttäjältä numerot ja muutetaan tyypiksi kokonaisluku
const number1 = parseInt(prompt("Input integer:"));
const number2 = parseInt(prompt("Input second integer:"));
const number3 = parseInt(prompt("Input third integer:"));

const sum = number1 + number2 + number3;       // summa
const product = number1 * number2 * number3;   // tulo
const average = sum / 3;                       // keskiarvo

// tulostetaan tulokset HTML-dokumenttiin
document.querySelector("#numbers").innerHTML = `Numbers: ${number1}, ${number2} and ${number3}`;
document.querySelector("#sum").innerHTML = `Sum: ${sum}`;
document.querySelector("#product").innerHTML = `Product: ${product}`;
document.querySelector("#average").innerHTML = `Average: ${average}`;
