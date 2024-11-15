// 3.2
// Open t2 folder in your IDE/editor. Add HTML by using createElement() and appendChild methods. (2p)
// Add the following HTML code to the element with id="target"
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
// Add class my-item to the second list item

const items = ["First item", "Second item", "Third item"];
const target = document.querySelector("#target");

for (let item of items) {

  // luodaan tyhjä li-elementti
  const liElement = document.createElement("li");

  // annetaan elementille sisältö
  liElement.innerHTML = item;

  // lisätään lapsi-elementti HTML-dokumenttiin
  target.appendChild(liElement);

  console.log(item)
  if (item === "Second item") {
    // lisätään luokka elementtiin
    liElement.classList.add("my-item");
  }
}
