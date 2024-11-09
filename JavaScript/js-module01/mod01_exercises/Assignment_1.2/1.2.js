// Assignment 1.2
// Write a program that prompts for user's name and then greets the user.
// Print the result to the HTML document: Hello, Name! (2p)

"use strict";
const name = prompt("Input your name:");

document.querySelector("#name").innerHTML = `Hello, ${name}!`;
