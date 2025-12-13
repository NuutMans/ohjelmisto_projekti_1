// Returns a random dice roll between 1 and 6
function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

// porgram
let result;

document.write("<ul>");

do {
  result = rollDice();
  document.write("<li>" + result + "</li>");
} while (result !== 6);

document.write("</ul>");