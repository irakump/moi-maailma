// Assignment 1.5
// Write a program that asks the user to enter a year and notifies the user whether the input year
// is a leap year. A year is a leap year if it is divisible by four. However, years divisible by
// 100 are leap years only if they are also divisible by 400. Print the result on the HTML document. (3p)

"use strict";

// pyydetään vuosi
const year = parseInt(prompt("Enter a year."));
let result;

// karkausvuosilaskuri
if (year % 4 === 0) {
  if (year % 100 === 0 && year % 400 !== 0) {
    result = "is not a leap year.";
  } else {
    result = "is a leap year.";
  }
} else {
  result = "is not a leap year.";
}

// tulostetaan HTML-dokumenttiin
document.querySelector("#year").innerHTML = `${year} ${result}`;
