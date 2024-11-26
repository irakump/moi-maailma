// 4.3
// Develop the app even further. Print the following information for all series
// from the search result on the web page. (7p)
// required information: Name, link to details (url), medium image and summary
// show the name in <h2> element
// show the url in <a> element. Also add target="_blank" to the link.
// show the medium image with <img src="" alt="">. Add medium image to src attribute
// and name property to alt attribute.
// some TV-shows don't have images. This will cause an error. You can fix this
// by adding ? operator to image property. Example: tvShow.show.image?.medium;.
// This is called optional chaining.
// show summary in <div> element (not <p>). This is because the summary is already
// in <p> element, and the result will not be valid if <p> is inside another <p>.
// collect the elements to <article> elements and append <article> elements to the HTML document.
// make <div id="results"> element to the HTML document where you append the <article> elements.
// clear the old results with innerHTML = '' before you append the new results.

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
      img.setAttribute("src", j.show.image?.medium)
      img.setAttribute("alt", j.show.name);
      div.innerHTML = j.show.summary;
    }

  } catch (error) {
    console.log(error.message);
  }

});
