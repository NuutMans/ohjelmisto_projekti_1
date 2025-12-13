// Function that returns a random dice roll between 1 and as many sides as is given
function rollDice(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

// Ask how many sides
const sides = Number(prompt("Enter number of sides on the dice:"));

let result;

document.write("<ul>");

do {
  result = rollDice(sides);
  document.write("<li>" + result + "</li>");
} while (result !== sides);

document.write("</ul>");