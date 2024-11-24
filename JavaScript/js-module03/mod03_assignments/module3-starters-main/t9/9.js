// 3.9
// This is continuation to previous task. There is only
// one text field left, where the user writes the calculation (addition, subtraction,
// multiplication or division) (4p)
// You can use the includes and split methods.
// eval() function is prohibited
// No need to support decimal numbers, calculating integers is enough.
// Example inputs: 3+5, 2-78, 3/6, etc...

"use strict";

const button = document.querySelector("#start");
button.addEventListener("click", function() {

  // määritetään muuttujat
  const userInput = document.getElementById("calculation");
  const inputValue = userInput.value;
  let result = 0;
  let operation = "";
  let inputArray = [];

  // käydään läpi syöte, tallennetaan luvut listaan
  if (inputValue.includes("+")) {
    operation = "+";
    inputArray = inputValue.split("+");
  } else if (inputValue.includes("-")) {
    operation = "-";
    inputArray = inputValue.split("-");
  } else if (inputValue.includes("*")) {
    operation = "*";
    console.log(operation);
    inputArray = inputValue.split("*");
  } else if (inputValue.includes("/")) {
    operation = "/";
    inputArray = inputValue.split("/");
  }

  // laskutoimitus

  // lisätään ensimmäinen alkio tulokseen
  result += parseFloat(inputArray[0]);

  // lasketaan muut luvut
  for (let i = 1; i < inputArray.length; i++) {
    if (operation === "+") {
      result += parseFloat(inputArray[i]);
    } else if (operation === "-") {
      result -= parseFloat(inputArray[i]);
    } else if (operation === "*") {
      result *= parseFloat(inputArray[i]);
    } else if (operation === "/") {
      result /= parseFloat(inputArray[i]);
    }
  }

  // tulostetaan tulos HTML-dokumenttiin
  const target = document.querySelector("#result")
  target.innerText = result;

});
