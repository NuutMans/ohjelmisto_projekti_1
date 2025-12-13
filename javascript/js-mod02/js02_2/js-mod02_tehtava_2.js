const count = Number(prompt("How many participants?"));
const participants = [];

// Ask for participant names
for (let i = 0; i < count; i++) {
  const name = prompt("Enter participant name " + (i + 1) + ":");
  participants.push(name);
}

// Sort names alphabetically
participants.sort();

// Print as an ordered list
document.write("<ol>");
for (let i = 0; i < participants.length; i++) {
  document.write("<li>" + participants[i] + "</li>");
}
document.write("</ol>");