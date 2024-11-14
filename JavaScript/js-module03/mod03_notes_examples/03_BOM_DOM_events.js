// Moduuli 3 - BOM, DOM & events

"use script";

// DOM - Document Object Model

// document on yksi olio, jonka metodeihin voi viitata (dokument."tässä joku juttu")

// haetaan viittaus johonkin solmuun (node) DOMissa eli
// haetaan viittaus HTML-dokumentin elementteihin (parametrina voi antaa merkkijonon samoin kuin css)
const h1Element = document.querySelector("h1");
console.log(h1Element)

/////// DOM:N MUOKKAUKSIA ///////

// tallennetaan HTML-dokumentin elementti muuttujaan
const title = h1Element.textContent;

// vaihdetaan elementissä oleva teksti (muuttujanNimi.textContent = "tähän teksti")
h1Element.textContent = title + " + lisäys otsikkoon"

// muokataan tyyliä
h1Element.style.fontSize = "22px";

// lisätään/näytetään elementti
h1Element.classList.add("text");

// piilotetaan elementti css:n avulla
h1Element.classList.add("hidden")

// näytetään taas eli poistetaan hidden-luokka?
h1Element.classList.remove("hidden")

// ylemmän tason parent-elementin piilotus (nyt parent = header)
h1Element.parentElement.classList.add("hidden");

// näytetään taas ylempi elementti = poistetaan luokka hidden
h1Element.parentElement.classList.remove("hidden");

// lisätään sisältöä sivulle; lisätään p-elementti
const pElement = document.createElement("p");
document.querySelector("main").append(pElement)
pElement.textContent = "Uusi kappale luotu JS-tiedostosta!"

// HTML-dokumentin voisi luoda kokonaan js-tiedostosta (siten, että HTML:ssä on yksi elementti, esim. body,
// jonne kaikki asiat luodaan js:n kautta)

// haetaan viittaus useampaan elementtiin/nodeen kerralla
const paragraphs = document.querySelectorAll("p");
console.log(paragraphs);

// muutetaan kappaleen sisältöä
paragraphs[2].textContent = "Kolmas kappale.";

// iteroidaan kaikki kappaleet läpi ja muutetaan tekstiä
// for (const p of paragraphs) {
//   console.log(p);
//   p.textContent = "päivitetty";
// }

// querySelectorilla saadaan valittua ensimmäinen "juttu"
// querySelectorAll: saadaan kaikki valittua

// tehdään järjestetty lista, jossa on 5 alkiota /////////// ks. tähän tuntiesimerkki!

const listContents = ["pencil", "rubber", "bag", "desc"];
// haetaan viittaus diviin id:n avulla
const listDiv = document.querySelector("#list");

// funktio jolla voi tulostaa taulukon sisällön ol-listaksi DOMiin
function renderList(items) {
  // tyhjennetää div ennen uuden ol-elementin lisäystä
  listDiv.innerHTML = "";
  olElement = document.createElement("ol");

  for (let i = 0; i < items.length; i++) {
    const newLi = document.createElement("li");
    newLi.textContent = items[i];
    olElement.append(newLi);
  }
  // lisätään luotu lista div-elementtiin
  listDiv.append(olElement);
}

// li-elementtien järjestyksen muuttaminen (muutetaan listan järjestystä)
//renderList(listContents);
listContents.push("laptop");

listContents.sort();


// BOM-rajapinta (window-olio)
// luetaan selaimen "sijainti" (url)
window.console.log(window.location.href)

// Tapahtumankäsittely eli eventit
// event = kaikki tapahtumat, joita käyttäjä tekee dokumentissa (esim. klikkaukset, kirjaimet..)
const printButton = document.getElementById("print");

// asetetaan napille tapahtumankäsittelijä click-eventille
printButton.addEventListener("click", function (event) {

  console.log("sort and print button clicked, event", event);
  listContents.sort();
  renderList(listContents);
})

// asioiden lisäys listalle
const addButton = document.querySelector("#add")
// asetetaan napille tapahtumankäsittelijä click-eventille
addButton.addEventListener("click", () => {
  const newItem = window.prompt("Lisää jotain listaan?")
  listContents.push(newItem);
  renderList(listContents);
});

// hiiritapahtumia
document.addEventListener("mousemove", function (event) {
  //console.log(event);
  document.querySelector("#output").textContent = `Hiiren
  osoittimen koordinaatit: ${event.clientX}, ${event.clientY}`;
  // näytetään h1, kun hiiri menee riittävän alas
  if (event.clientY > 200) {
    h1Element.classList.remove("hidden");
  }
});

h1Element.addEventListener("mouseenter", function(){
  // piilotetaan elementti css avulla, kun hiiren osoitin menee sen päälle
  h1Element.classList.add("hidden");
})

// Näppäimistö-eventti "toggle" (h piilottaa ja näyttää koko sivun)
const keyLog = [];
let hidden = false;
document.addEventListener("keypress", function (event) {

  keyLog.push(event.key);
  console.log("logi", keyLog)
  if (event.key === "h") {
    if (!hidden) {
      document.querySelector("body").classList.add("hidden");
    } else {
      document.querySelector("body").classList.remove("hidden");
    }
    hidden = !hidden;
  }
});

// tapahtumakäsittelyt: ainoa oikea tapa javascriptissä on addEventListener !!!!! (muut vanhoja)


/*
-------LOOPEISTA------
- kannattaa käyttää for/of-looppia silloin, kun ei tarvitse iteroida
- for/in-loop toimii eri tavalla (miten??), ehkä olioiden kanssa?
- jos tarvitsee iteraattorin, käytä for/i-looppia
 */

/////////////////////////////////////////////////////










