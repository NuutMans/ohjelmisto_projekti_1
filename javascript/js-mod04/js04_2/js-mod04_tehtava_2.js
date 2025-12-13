const form = document.getElementById("searchForm");
const input = document.getElementById("query");

form.addEventListener("submit", function (event) {
  event.preventDefault(); // prevent page reload

  const searchTerm = input.value;
  const url = `https://api.tvmaze.com/search/shows?q=${searchTerm}`;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data); // print search result to console
    })
    .catch(error => {
      console.error("Error:", error);
    });
});