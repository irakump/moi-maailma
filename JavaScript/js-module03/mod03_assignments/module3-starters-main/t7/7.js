// Make a hover effect with JavaScript. (2p)
// when user mouses over <p id="trigger"> change the picture of <img id="target"> form picA.jpg to picB.jpg
// when user mouses off, change the picture back to original

"use strict";


const trigger = document.querySelector("#trigger");
// vaihdetaan kuva A:sta B:hen - mouseenter
trigger.addEventListener("mouseenter", function(event) {
  document.getElementById("target").src = "img/picB.jpg";
  document.getElementById("target").setAttribute("src", "img/picB.jpg");
});

// vaihdetaan kuva B:stä A:han - mouseleave
trigger.addEventListener("mouseleave", function(event) {
  document.getElementById("target").src = "img/picA.jpg";
  document.getElementById("target").setAttribute("src", "img/picA.jpg");
})
