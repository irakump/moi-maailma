// 3.1
// Open t1 folder in your IDE/editor. Add HTML by using innerHTML property (2p)
// Add the following HTML code to the element with id="target"
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
// Add class my-list to the element with id="target"

const items = ["First item", "Second item", "Third item"];
const target = document.querySelector("#target");

for (item of items) {
  // luodaan tyhjä li-elementti
  let liElement = document.createElement("li");

  // annetaan elementille sisältö
  liElement.innerHTML = item;

  // lisätään lapsi-elementti HTML-dokumenttiin
  target.appendChild(liElement);
}

// lisätään luokka elementtiin
target.classList.add("my-list")
