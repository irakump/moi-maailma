// 4.1
// Make an app that retrieves information about a TV series you enter and displays
// it in the console. (2p)
// API to use: TVMaze API
// First, make a valid HTML page with a search form. Example form:
// <form action="https://api.tvmaze.com/search/shows">
//   <input id="query" name="q" type="text">
//   <input type="submit" value="Search">
// </form>
// Test the form. The result should be a page full of JSON formatted data.

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



