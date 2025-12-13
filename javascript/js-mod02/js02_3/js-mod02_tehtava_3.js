const dogs = [];

// Name 6 dogs
for (let i = 0; i < 6; i++) {
  const name = prompt("Enter dog name " + (i + 1) + ":");
  dogs.push(name);
}

// Sort alphabetically and reverse
dogs.sort();
dogs.reverse();

// Print as list
document.write("<ul>");
for (let i = 0; i < dogs.length; i++) {
  document.write("<li>" + dogs[i] + "</li>");
}
document.write("</ul>");