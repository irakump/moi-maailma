// Assignment 2.10
// Write a voting program as described below for small-scale meeting use. (8p)
// The program asks for the number of candidates. Then the program asks for the names
// of the candidates: 'Name for candidate 1'. Store the candidates' names and initial
// vote count in objects like this:
// [{name: 'ellie', votes: 0,}, {name: 'frank', votes: 0}, {name: 'pamela', votes: 0,},]

// The program asks for the number of voters.
// The program asks each voter in turn who they will vote for. Voter should enter candidate
// name. If the voter enters an empty value instead of the voting name, it will be interpreted
// as an empty vote. The program announces the name of the winner and the results by printing
// it to the console:
// The winner is pamela with 3 votes.
// results:
// pamela: 3 votes
// frank: 1 votes
// ellie: 1 votes

// Some help:
  // You need to compare votes so console log a and b to see how to get the correct property.
/*
    someArray.sort((a, b) => {
    console.log(a, b);
    return b - a;
 });
*/

"use strict";

// tyhjä taulukko ehdokkaille
const candidates = [];

// pyydetään ehdokkaiden lukumäärä
const candidateAmount = parseInt(prompt("Enter the number of candidates."))

// pyydetään nimet
for (let i = 1; i <= candidateAmount; i++) {
  let name = prompt(`Name for candidate ${i}.`)

  // tallennetaan ehdokkaan nimi ja äänet oliona taulukkoon
  const candidate = {
  name: name,
  votes: 0,
  }
  candidates.push(candidate);
}

// tulostetaan ehdokkaat konsoliin:
console.log("Candidates:")
for (let i = 0; i < candidateAmount; i++) {
  console.log(candidates[i].name)
}

// pyydetään äänestäjien määrä
const voteAmount = parseInt(prompt("Enter the number of voters."))

// äänestyskierros
for (let i = 1; i <= voteAmount; i++) {
  const vote = prompt(`Vote ${i}. Who will you vote for? Enter the name.`)
  if (vote !== "") {

    // jos nimi on taulukossa, lisätään ääni
    for (let i = 0; i < candidateAmount ; i++) {
      if (candidates[i].name === vote) {
        candidates[i].votes++;
      }
    }
  } else {
    alert("Empty vote.");
  }
}

// järjestetään oliot äänimäärän mukaan laskevaan järjestykseen
candidates.sort((a, b) => {
   //console.log(a.votes, b.votes);
   return b.votes - a.votes;
});

// tulosten julkistus
console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.`);
console.log("results:")
for (let i = 0; i < candidateAmount; i++) {
  console.log(`${candidates[i].name}: ${candidates[i].votes} votes`)
}
