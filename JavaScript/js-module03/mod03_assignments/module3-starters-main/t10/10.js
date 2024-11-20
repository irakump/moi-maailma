// 3.10
// Read the first name and last name values from the form and
// print them in the <p id="target"> (2p)
// remember to stop the default action of the form
// you can use attribute selectors in querySelector() to select the <input> elements
// example output: Your name is Luke Skywalker

"use strict";

// tallennetaan käyttäjän syöttämät arvot muuttujiin
const firstName = document.querySelector("input[name=firstname]");
const lastName = document.querySelector("input[name=lastname]");

// stop the default action of the form
const form = document.getElementById("source");
form.addEventListener("submit", function(event) {
  event.preventDefault();
  // tulostetaan nimi p-elementtiin
  const target = document.getElementById("target");
  target.innerText = `Your name is ${firstName.value} ${lastName.value}`;
});
