const num1 = parseInt(prompt("Enter first integer:"));
const num2 = parseInt(prompt("Enter second integer:"));
const num3 = parseInt(prompt("Enter third integer:"));

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

document.write("Sum: " + sum + "<br>");
document.write("Product: " + product + "<br>");
document.write("Average: " + average);