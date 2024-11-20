// 3.8
// Make a simple calculator. (4p)
// There are two input fields where user enters numbers. Based on the drop-down list, calculator
// performs addition, subtraction, multiplication or division of these two numbers.

"use strict";

// tallennetaan arvoja muuttujiin
const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const selectElement = document.getElementById("operation");

const calculate = document.querySelector("#start");
calculate.addEventListener("click", function() {
  // muutetaan merkkijonot luvuiksi
  const value1 = parseInt(num1.value);
  const value2 = parseInt(num2.value);

  const operation = selectElement.value;
  let result;

  // lasketaan tulos
  if (operation === "add") {
    result = value1 + value2;
  } else if (operation === "sub") {
    result = value1 - value2;
  } else if (operation === "multi") {
    result = value1 * value2;
  } else if (operation === "div") {
    result = value1 / value2;
  }
  // tulostetaan HTML-dokumenttiin
  const resultHTML = document.querySelector("#result");
  resultHTML.textContent = result;
});
