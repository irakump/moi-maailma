// Moduuli 3 - BOM, DOM & events

"use script";

// DOM - Document Object Model

// document on yksi olio, jonka metodeihin voi viitata (document."tässä joku juttu")

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

// näytetään taas eli poistetaan hidden-luokka
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

// tehdään järjestetty lista, jossa on 5 alkiota

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
printButton.addEventListener("click", function(event) {

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
document.addEventListener("mousemove", function(event) {
  //console.log(event);
  document.querySelector("#output").textContent = `Hiiren
  osoittimen koordinaatit: ${event.clientX}, ${event.clientY}`;
  // näytetään h1, kun hiiri menee riittävän alas
  if (event.clientY > 200) {
    h1Element.classList.remove("hidden");
  }
});

h1Element.addEventListener("mouseenter", function() {
  // piilotetaan elementti css avulla, kun hiiren osoitin menee sen päälle
  h1Element.classList.add("hidden");
})

// Näppäimistö-eventti "toggle" (h piilottaa ja näyttää koko sivun)
const keyLog = [];
let hidden = false;
//document.addEventListener("keypress", function (event) {
//
//  keyLog.push(event.key);
//  console.log("logi", keyLog)
//  if (event.key === "h") {
//    if (!hidden) {
//      document.querySelector("body").classList.add("hidden");
//    } else {
//      document.querySelector("body").classList.remove("hidden");
//    }
//    hidden = !hidden;
//  }
//});

// tapahtumakäsittelyt: ainoa oikea tapa javascriptissä on addEventListener !!!!! (muut vanhoja)

// Oletustapahtuma ja sen estäminen
// estetään formin automaattinen lähetys (sivun päivitys)
const form = document.querySelector('form');
const fname = document.querySelector("input[name=fName]");
const lname = document.querySelector("input[name=lName]");

// kun lähettää lomakkeen, tulostetaan muuttujien arvot konsoliin
// TÄTÄ VOISI KÄYTTÄÄ LENTOPELISSÄ?? (kun syöttää seuraavan lentokentän icaon / numeron tms.)
form.addEventListener('submit', function(event) {
  event.preventDefault();
  console.log(event);
  console.log(`Etunimi: `, fname.value);
  console.log(`Sukunimi:`, lname.value);
})


// NAVIGATOR-INTERFACE - tuntimuistiinpanot

// navigaattorin avulla voi lisätä koordinaatit / kartan, jossa näkyy oma sijainti


// Options for retrieving location information (optional)
const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};

// A function that is called when location information is retrieved
function success(pos) {
  const crd = pos.coords;

  // Printing location information to the console
  console.log('Your current position is:');
  console.log(`Latitude : ${crd.latitude}`);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);

  // Use the leaflet.js library to show the location on the map (https://leafletjs.com/)
  const map = L.map('map').setView([crd.latitude, crd.longitude], 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  L.marker([crd.latitude, crd.longitude]).
      addTo(map).
      bindPopup('I am here.').
      openPopup();
}

// Function to be called if an error occurs while retrieving location information
function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

// Starts the location search
navigator.geolocation.getCurrentPosition(success, error, options);


/*
-------LOOPEISTA------
- kannattaa käyttää for/of-looppia silloin, kun ei tarvitse iteroida
- for/in-loop toimii eri tavalla (miten??), ehkä olioiden kanssa?
- jos tarvitsee iteraattorin, käytä for/i-looppia
 */

/////////////////////////////////////////////////////

// MUISTIINPANOT MATERIAALISTA:
/*
-window = selainikkuna, tuettu kaikissa selaimissa
-kaikki globaalit javascript-oliot, funktiot ja muuttujat ovat automaattisesti
  ikkuna-käyttöliittymän jäseniä (window interface)
  esim. window.document.querySelector(".button") on sama kuin
        document.querySelector(".button")   --> eli ei tarvitse kirjoittaa alkuun window

- alert() -funktio = avaa pop-up-ikkunan, jossa on teksti ja ok-nappi. Voi antaa käyttäjälle
  tiedon, esim. jos joku toiminto onnistuu tai epäonnistuu. Ohjelma on pysähdyksissä,
  kunnes käyttäjä painaa OK
  alert("Some text here");

- confirm() -funktio avaa pop-up-ikkunan, jossa on kaksi nappia: OK ja Cancel
  --> käyttäjä voi valita, suoritetaanko joku toiminto vai ei
  esim.
  const answer = confirm("Some question");
  // vastauksen tulostus konsoliin:
  console.log(answer);

  --> käyttäjän vastaus tallennetaan answer-muuttujaan boolean arvona true (= OK) tai false (= Cancel)

- prompt() -funktio avaa pop-up-ikkunan, johon käyttäjä voi antaa syötteen
  const answer = prompt("Title", "Initial content for the text field")
  --> ensimmäinen "parametri" eli title: otsikko pop-up-ikkunassa
  --> toinen "parametri?" eli initial content... on vapaaehtoinen (=default, oletusarvo)
      on valmiina kirjoitusruudussa, voisi esim. olla "write answer here" tms.

  --> jos käyttäjä ei syötä mitään, answer-muuttujan arvo on null

NAVIGATOR-INTERFACE (navigaattori-käyttöliittymä)
- voi hakea tietoa selaimesta
- navigator.geolocation palauttaa laitteen gps-koordinaatit
  --> ks. HTML-tiedostosta koodi (tulostaa kartan, johon sijainti merkitty)
          --> sen käyttö lentopelissä!

LOCATION-INTERFACE
- käyttöliittymä kertoo dokumentin osoitteen, usein käytetään selaimen "uudelleen ohjaamiseen"
  esim.
  location.href = "http://metropolia.fi";

 */

alert("Moikkamoi")
const answer = confirm("Do you want to add a member to the list?")
console.log(`User answer to adding: ${answer}`)

const answer1 = prompt("Input your name", "name")

/*
DOM = Document Object Model
- HTML-dokumentin "puukaavio"-kuvaus
- DOM = standardi, joka määrittää, miten HTML-elementtejä valitaan, muokataan, lisätään
  tai poistetaan
- kaikki elementit, attribuutit ja sisältö (esim. teksti) = node = solmu

-kaavio:
          Document
              |
        root    element:    <html>
        |                     |
    Element:                 Element:
    <head>                    <body>
      |                     /          \
element:   Attribute: ---- element:     element:
<title>      "href"         <a>            <h1>
  |                          |               |
 Text:                      Text:           Text:
"My title"                 "My link"      "My header"


-parent/child + sibling (aikuinen/lapsi):
  -h1-elementti on body-elementin lapsi sekä a-elementin sisarus
  --> eli elementin "seuraava" elementti on aina lapsi, ja "samanarvoinen" vierekkäinen elementti sisarus
  -body-elementti on sekä h1- että a-elementin vanhempi


DOCUMENT-INTERFACE
- document-käyttöliittymä edustaa nettisivua
- sisältää kaikki muut oliot (kohteet)
- jos haluaa valita minkä tahansa HTML-elementin dokumentista, pitää aloittaa document-(käyttö)liittymästä
  esim.
  document.getElementbyID("logo");    --> tässä haetaan elementt, jonka id on logo

  TÄRKEIMMÄT FUNKTIOT JA TOIMINNOT:

  - haetaan yksi elementti id:n perusteella (css-selectorin avulla)
    --> voisi hakea yhden elementin myös luokan perusteella (".logo"), luokka jonka nimi on logo
  document.querySelector("#logo")

  - haetaan kaikki elementit, joissa on sama luokka (css-luokkaselektorin avulla)
  document.querySelectorAll(".button")

  -haetaan yksi elementti sen id:n perustaalla
  document.getElementById("#logo")

  --käskyjä voi kohdistaa valittuun elementtiin:

  -haetaan kaikki p-elementit valitusta elementistä
  element.getElementsByTagName("p")
  --> getElementsByTagName palauttaa taulukon, indeksit alkaa nollasta (samoin kuin pythonin listoissa)

  -lisätään lapsi-node (solmu) elementtiin
  element.appendChild(child)

  -poistetaan lapsi-node
  element.removeChild(child)

  -lisätään HTML-koodi elementtiin
  element.innerHTML

  -lisätään teksti elementtiin
  element.innerText

 */

// ESIMERKKEJÄ:
// https://github.com/ilkkamtk/JavaScript-english/blob/main/BOM-DOM-event.md#examples

// toggle = vaihtaa

/*

EVENT handling (käsittely)
- käsitellään käyttäjän toimintoja ja vastauksia
- esim. käyttäjä painaa nappia, javascriptillä voi näyttää infoboksin

<button>Click me</button>
<script>
const button = document.querySelector('button');
button.addEventListener('click', function(evt){
  alert('Element ' + evt.currentTarget.tagName + ' was clicked');
});
</script>

- event handleria kutsutaan myös callback-funktioksi:
  https://github.com/ilkkamtk/JavaScript-english/blob/main/extras.md#callback-functions-and-callback-hell

- lisää infoa eventistä: https://developer.mozilla.org/en-US/docs/Web/API/Event

- mouse related events: https://developer.mozilla.org/en-US/docs/Web/API/Element#mouse_events

- syntax (3 tapaa eventin käsittelyyn: vanha (90-luku), perinteinen (2000-luku), nykyaikainen)

  - modern: addEventListener (tätä kannattaa käyttää, ei muita / vanhempia tapoja!)

esim.

<button>Click me</button>
<script>
    const button = document.querySelector('button');

function A(evt){
  alert('This is function A');
  nappi.removeEventListener('click', A);
  nappi.addEventListener('click', B);
}

function B(evt){
  alert('This is function B');
}

nappi.addEventListener('click', A);
</script>

// mouseenter -event: kun hiiri tulee elementin päälle, tapahtuu jokin asia
// mouseleave -event: kun hiiri poistuu elementin päältä

-- OLETUSTAPAHTUMAN PYSÄYTTÄMINEN (stopping default action of an event)

  - joillakin elementeillä, esim. <a> tai <form>, on oletustapahtumia (default actions)
    esim. <a> -elementti vie osoitteeseen, joka on merkitty href-attribuuttiin (linkki)
          <form> -elementti avaa osoitteen, joka on merkitty action-attribuuttiin, kun lomake lähetetään

  - esim. kun täyttää ja lähettää lomakkeen, oletuksena esim. uusi osoite avautuu uuteen ikkunaan
    --> toiminto halutaan estää

  - preventDefault -funktio estää oletustoiminnot:
  esim.

<form>
  <div>
    <input name="fName" type="text" placeholder="first name">
  </div>
  <div>
    <input name="lName" type="text" placeholder="last name">
  </div>
  <div>
    <input name="submit" type="submit" value="Send">
  </div>
</form>
<p></p>

<script>
// select the elements
const form = document.querySelector('form');
const fname = document.querySelector('input[name=fName]');
const lname = document.querySelector('input[name=lName]');
const p = document.querySelector('p');

// When the form is submitted...
form.addEventListener('submit', function(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // Here you can check, for example, whether the fields on the form have been filled in correctly,
    // after which it could be sent using the fetch method, for example
    // However, for now, let's print the user input as an example.
    p.innerText = `Your name is ${fname.value} ${lname.value}`;
});
</script>

 */

///////////////////////
// muistiinpanoja

// tietoa voi hakea koko dokumentista tai jostakin sen osasta, jolloin ohjelman
// ei tarvitse käydä läpi koko dokumenttia:

// testi, tallennetaan main-elementti
const main = document.querySelector("main");
// haetaan main-elementistä section-elementti
const section1 = main.querySelector("section");

// aina kun tulee virhe, ks. console (näyttää virheet)!

// kaksi (kolme) tapaa lisätä tekstiä:
// element.innerHTML = "";    // tämä silloin, jos haluaa lisätä html:ää
// element.innerText = "";    // voi asettaa pelkkää tekstiä, palauttaa näkyvän tekstin
// element.textContent = "";  // palauttaa sekä näkyvän että piilotetun tekstin

// attribuutin lisääminen elementtiin, 2 tapaa:
// element.setAttribute("src", "test.png");
// element.src = "test.png";

///////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////

// testi - footerille event
//const footer = document.querySelector("footer");
//footer.addEventListener("click", function(event) {
//  alert("You clicked footer!")
//})


// querySelector on css-komento, document käy koko HTML-dokumentin läpi (document.querySelector)

  // luodaan elementti img
  let i = document.createElement("img");

  // lisätään attribuutti (notaatiolla)   // voisi tehdä myös i.setAttribute
  //i.src = pic.image.medium;

  // toinen tapa asettaa kuva:
  //i.setAttribute("src", pic.image.medium);

// 3.9 tehtävän muistiinpanoja - INCLUDES() JA SPLIT() -metodit
// includes-metodilla voi kokeilla, onko jokin termi listassa
// array.includes(termi)
// voisiko tehdä niin, että tallentaa inputin merkkijonoksi, ja käy kirjaimet läpi includesilla,
//  ja jos on +, tulee summa, jos -, miinuslasku jne?

// split()
// split() splits a string into an array of substrings, and returns the array:
// let text = "How are you doing today?";
// const myArray = text.split(" ");
// How,are,you,doing,today?
// eli ensin split() -metodi ja sitten includes()

// metodeilla voi myös käydä läpi käyttäjän syötteen, esim. "2+13", ei tarvitse olla listassa

// toinen esim, split()
let text = "Heipparallaa!";
const array1 = text.split("");
console.log("Tulostan taulukon: ")
for (const index of array1) {
  console.log(index);           // tulostuu yksi kirjain kerrallaan
}
