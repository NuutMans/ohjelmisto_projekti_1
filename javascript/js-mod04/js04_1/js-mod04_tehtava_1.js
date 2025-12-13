const form = document.getElementById("searchForm");
const queryInput = document.getElementById("query");

form.addEventListener("submit", function (event) {
  event.preventDefault(); // stop page reload

  const query = queryInput.value;
  const url = "https://api.tvmaze.com/search/shows?q=" + query;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      console.log(data); // show result in console
    })
    .catch(error => {
      console.error("Error:", error);
    });
});
