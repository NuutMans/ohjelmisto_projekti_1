const numbers = [];
let input;

while (true) {
  input = Number(prompt("Enter a number:"));

  // Check if number exists
  if (numbers.includes(input)) {
    console.log(input + " has already been given.");
    break;
  }

  numbers.push(input);
}

// Sort numbers ascending
numbers.sort((a, b) => a - b);

// Print to console
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}