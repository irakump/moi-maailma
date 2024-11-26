// 4.4
// Develop the app even further. Optional chaining is not the best way to handle
// missing image. Use ternary operator or if/else to add a default image if TV-show
// is missing image property. (2p)
// Use https://via.placeholder.com/210x295?text=Not%20Found as the default image.

"use strict";

const form = document.querySelector("form");
form.addEventListener("submit", async function (event) {

  try {
    event.preventDefault();

    // haetaan käyttäjän syöte dokumentista
    const userInput = document.querySelector("#input");
    const value = userInput.value;

    // haetaan vastaus
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value}`);
    const jsonData = await response.json();

    // tyhjennetään elementti sisällöstä
    const results = document.querySelector("#results");
    results.innerHTML = "";

    for (const j of jsonData) {
      // luodaan elementit ja dokumentin rakenne
      const ar = document.createElement("article");
      results.appendChild(ar);
      const h2 = document.createElement("h2");
      ar.appendChild(h2);
      const a = document.createElement("a");
      ar.appendChild(a);
      const img = document.createElement("img");
      ar.appendChild(img);
      const div = document.createElement("div");
      ar.appendChild(div);

      // lisätään elementeille arvot
      h2.innerHTML = j.show.name;
      a.setAttribute("target", "_blank");
      const url = j.show.url;
      a.setAttribute("href", url);

      // lisätään (medium-kokoinen) kuva jos on, muuten placeholder
      if (j.show.image && j.show.image.medium) {
        img.setAttribute("src", j.show.image?.medium);
      } else {
        img.setAttribute("src", "https://via.placeholder.com/210x295?text=Not%20Found");
      }
      img.setAttribute("alt", j.show.name);
      div.innerHTML = j.show.summary;
      }
    } catch (error) {
    console.log(error.message);
  }

});
