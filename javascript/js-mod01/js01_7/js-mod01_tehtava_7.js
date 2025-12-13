const rolls = Number(prompt("How many dice rolls?"));
let sum = 0;

for (let i = 0; i < rolls; i++) {
  // Roll a die (1–6)
  const die = Math.floor(Math.random() * 6) + 1;
  sum += die;
}

document.write("Sum of dice rolls: " + sum);