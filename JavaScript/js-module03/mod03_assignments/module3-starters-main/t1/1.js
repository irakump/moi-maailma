// 3.1
// Open t1 folder in your IDE/editor. Add HTML by using innerHTML property (2p)
// Add the following HTML code to the element with id="target"
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
// Add class my-list to the element with id="target"

const items = ["First item", "Second item", "Third item"];
const target = document.querySelector("#target");
let inner = "";

// luodaan merkkijono
for (let item of items) {
  inner += `<li>${item}</li>`;
}

// lisätään merkkijono HTML-dokumenttiin
document.querySelector("#target").innerHTML = inner;

// lisätään luokka elementtiin
target.classList.add("my-list")
