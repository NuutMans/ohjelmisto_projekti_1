const form = document.getElementById("searchForm");
const queryInput = document.getElementById("query");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const query = queryInput.value;
  const url = `https://api.tvmaze.com/search/shows?q=${query}`;

  fetch(url)
    .then(response => response.json())
    .then(data => {

      resultsDiv.innerHTML = "";

      data.forEach(item => {
        const show = item.show;

        const article = document.createElement("article");

        const name = document.createElement("h2");
        name.textContent = show.name;

        const link = document.createElement("a");
        link.href = show.url;
        link.textContent = show.url;
        link.target = "_blank";

        const image = document.createElement("img");

        if (show.image) {
          image.src = show.image.medium;
        } else {
          image.src = "https://placehold.co/210x295?text=Not%20Found";
        }

        image.alt = show.name;

        const summary = document.createElement("div");
        summary.innerHTML = show.summary || "No summary available.";

        article.appendChild(name);
        article.appendChild(link);
        article.appendChild(image);
        article.appendChild(summary);

        resultsDiv.appendChild(article);
      });
    })
    .catch(error => {
      console.error("Error:", error);
    });
});