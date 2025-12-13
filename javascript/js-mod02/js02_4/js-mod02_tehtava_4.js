const numbers = [];
let input;

do {
  input = Number(prompt("Enter a number (0 to stop):"));
  if (input !== 0) {
    numbers.push(input);
  }
} while (input !== 0);

// Sort numbers from largest to smallest
numbers.sort((a, b) => b - a);

// Print to console
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}