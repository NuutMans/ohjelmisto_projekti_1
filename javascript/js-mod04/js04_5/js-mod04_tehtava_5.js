fetch("https://api.chucknorris.io/jokes/random")
  .then(response => response.json())
  .then(data => {
    console.log(data.value); // print only the joke
  })
  .catch(error => {
    console.error("Error:", error);
  });