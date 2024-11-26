// 4.2
// Develop the app further.
// Add JavaScript that gets the value entered to the form and sends a request with fetch
// to https://api.tvmaze.com/search/shows?q=${value_from_input}. Print the search result
// to the console. (3p)

"use strict";

const form = document.querySelector("form");
form.addEventListener("submit", async function (event) {

  try {
    event.preventDefault();
    const userInput = document.querySelector("#input");
    const value = userInput.value;
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value}`);
    const jsonData = await response.json();

    // tulostetaan kaikki taulukossa olevat tulokset konsoliin
    for (const j of jsonData) {
      console.log(j.show);
    }
  } catch (error) {
    console.log(error.message);
  }

});
