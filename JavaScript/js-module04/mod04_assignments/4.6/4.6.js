// 4.6
// Develop the app further (4p).
// Now add a form where you can enter a search term like in assignments 1-3
// Send the search term to https://api.chucknorris.io/jokes/search?query=${value_from_input} using fetch()
// Print each joke in this format:
// <article>
//     <p>Joke here<p>
// </article>

"use strict";

function getAJoke() {
  try {
    const form = document.querySelector("form");
    form.addEventListener("submit", async function(event) {
      event.preventDefault();
      const input = document.querySelector("#value");
      const inputValue = input.value;
      const url = await fetch(
          `https://api.chucknorris.io/jokes/search?query=${inputValue}`);
      const jsonData = await url.json();

      // luodaan jokaiselle vitsille elementit ja sijoitetaan arvot
      const body = document.querySelector("body");
      const div = document.createElement("div");
      body.appendChild(div);
      div.setAttribute("id", "results");
      const results = document.getElementById("results");

      // tyhjennetään elementti
      results.innerHTML = "";

      for (const j of jsonData.result) {
        const a = document.createElement("article");
        results.appendChild(a);
        const p = document.createElement("p");
        a.appendChild(p);
        p.innerHTML = j.value;
        }

  });
  } catch (error) {
    console.error(error.message);
  }
}

getAJoke();
