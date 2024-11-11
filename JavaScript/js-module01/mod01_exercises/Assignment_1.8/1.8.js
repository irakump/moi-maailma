// Assignment 1.8
// Write a program that prompts the user for the start and end year. The program
// prints all leap years from the interval given by the user. Printing is done in
// an unordered list to the HTML document. (3p)

/*
Example output HTML code:
<ul>
    <li>1992</li>
    <li>1996</li>
    <li>2000</li>
    <li>2004</li>
    <li>2008</li>
</ul>
 */

"use strict";

// pyydetään vuodet
const firstYear = parseInt(prompt("Enter start year."));
const secondYear = parseInt(prompt("Enter end year."));

let year, result, i = 0;
const years = [];

// käydään läpi käyttäjän syöttämä aikaväli
for (year = firstYear; year <= secondYear; year++) {
    // karkausvuosilaskuri
    if (year % 4 === 0) {
      if (year % 100 === 0 && year % 400 !== 0) {
        result = "is not a leap year.";
      } else {
        result = "is a leap year";
        // lisätään karkausvuosi listaan
        years[i] = year;
        i++;
      }
    } else {
      result = "is not a leap year.";
    }
    // tulostetaan tulos konsoliin
    console.log(`${year} ${result}`);
}

let yearListHTML = "";

// tallennetaan karkausvuodet yhteen muuttujaan
for (let y in years) {
  yearListHTML += `<li>${years[y]}</li>`;
}
// tulostetaan karkausvuodet listana HTML-dokumenttiin
document.querySelector("#yearList").innerHTML = yearListHTML
