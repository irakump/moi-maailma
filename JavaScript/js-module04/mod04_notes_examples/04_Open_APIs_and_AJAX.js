// MODUULI 4 - Open APIs and AJAX

"use strict";

// [Client: HTML/CSS] JS -------HTTP-request-----> [Server: Py/Flask]
//                   <-------HTTP-response--------------/


// Open application programming interfaces: API, AJAX
// API = Application programming interface

// AJAX = Asynchronous JavaScript and XML
/*

A = Asynchronous
J = JavaScript
X = XML, eXtensible Markup Language

 */

// PROMISE = lupaus, object, joka palauttaa tietyn arvon
//  3 tasoa: fulfilled, rejected, pending

// FETCH() - hakee tiedoston json-muodossa

// tiedon hakeminen, jos tiedosto on samassa kansiossa: nimi riittää
fetch("pics.json");

// funktio, joka hakee kuvia tiedostosta, async, await (odottaa latauksen)
async function fetchImages() {
  const response = await fetch("pics.json");

  // jos response (vastaus) ok, eli statuskoodi 200 (2xx), suoritetaan seuraava
  if (response.ok) {
    const pics = await response.json();
    console.log("Pictures: ", pics);

    // luodaan img-elementit, lisätään kuvat elementtinä sectioniin
    for (const pic of pics) {
      const imgElement = document.createElement("img");
      imgElement.src = pic.address;
      imgElement.alt = pic.description;
      document.querySelector("#images").append(imgElement);
    }

  }

}


// jos tiedosto tms. on selaimessa, kirjoita koko osoite:
fetch("https://api.chucknorris.io/jokes/random");



// Chuck Norris api -esimerkki
console.log("script start");

async function getAJoke() {
  // virheen käsittely: try - catch (vastaa samaa kuin pythonin try - except)
  const outputElem = document.querySelector("#joke");
  try {
    const response = await fetch("https://api.chucknorris.io/jokes/random");

    if (!response.ok) {
      // negaatio, eli response on jotain muuta kuin ok (eli ei ole 200-alkuinen)
      throw new Error(response.status.toString());    // statuskoodi on numero, muutetaan merkkijonoksi (string)
    }
    // status-koodi ok (2xx) eli 200-aluinen
    const joke = await response.json()    // response.json() on asynkroninen operaatio, tarvitsee awaitin!
    console.log("vitsi: ", joke.value);
    outputElem.textContent = joke.value;

  } catch (error) {
    // errorin tulostus konsoliin: ei console.log, vaan console.error (toimisi myös logilla)
    console.error(error);
    outputElem.textContent = "Vitsin haku epäonnistui";
  }
}
// haetaan vitsi vain käyttäjän pyynnöstä (painaa nappia)
document.querySelector("#get-joke")
  .addEventListener("click", getAJoke);   // funktiossa ei sulkeita (eli getAJoke() ), koska sitä kutsutaan vain silloin kun
                                                // nappia painetaan

// esimerkki oman flask-serverin käytöstä

async function fetchAirport(icao) {
  // tähän voisi lisätä virheenkäsittelyn
  const response = await fetch("http://localhost:5000/airport/" + icao);
  const airport = await response.json();
  console.log("airport data: ", airport);
  // TO DO: add data to dom (näytä käyttäjälle)
  return airport;
}

// ks. tähän tuntiesimerkki serveristä (python-kansioon)

//fetchAirport(efhk);

const form = document.querySelector("#airport-form");
form.addEventListener("submit", async function (event) {
  // estetään lomakkeen oletustoiminnallisuus (eli oletuksena selain lisää lomakkeen arvot
  //    verkkosivun "hakusanoiksi")
  event.preventDefault();
  // haetaan viittaus input-elementtiin ja sen arvo (käyttäjän syöte)
  const userInput = form.querySelector("input").value;

  const airport = fetchAirport(userInput);    // tämä ei toimi - johtuuko serveristä? kesken
  console.log(airport);
});



// jos console logilla tulee "promise", puuttuu jostakin kohdasta awate -sana???




// muistiinpanoja

// await = odottaa, että fetch tms. suorittaa tehtävänsä loppuun. Awaitia voi käyttää vain asynkronisen funktion kanssa
// eli pitää olla async function, ja sen sisällä await fetch()
// joke:n arvo sijoitetaan vasta, kun response.json() on valmis, siitä kertoo await
// async = ohjelma ei jää odottamaan latausta, vaan jatkaa suoritusta funktion jälkeisestä kohdasta
// --> siksi konsolissa on script start, script end ja vasta sitten vitsi. Script end ehditään suorittaa ennen vitsin hakua
// response.json()    eli .json() palauttaa promisen

getAJoke();
fetchImages();

/////////////////////////////////////

// lue mod4 materiaalit JA  https://leafletjs.com/examples/quick-start/









console.log("script end");


