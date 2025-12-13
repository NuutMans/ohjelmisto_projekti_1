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
      // Clear results
      resultsDiv.innerHTML = "";

      data.forEach(item => {
        const show = item.show;

        // New article
        const article = document.createElement("article");

        const name = document.createElement("h2");
        name.textContent = show.name;

        const link = document.createElement("a");
        link.href = show.url;
        link.textContent = show.url;
        link.target = "_blank";

        const image = document.createElement("img");
        image.src = show.image?.medium || "";
        image.alt = show.name;

        const summary = document.createElement("div");
        summary.innerHTML = show.summary || "No summary available.";

        // Append
        article.appendChild(name);
        article.appendChild(link);
        article.appendChild(image);
        article.appendChild(summary);

        // Append article to results
        resultsDiv.appendChild(article);
      });
    })
    .catch(error => {
      console.error("Error:", error);
    });
});