const topNewsSection = document.getElementById("topNews");
const resultsDiv = document.getElementById("results");

document.addEventListener("DOMContentLoaded", async () => {
  try {
    const res = await fetch("https://api.spaceflightnewsapi.net/v4/articles");
    const data = await res.json();
    const top3 = data.results.slice(0, 3);

    top3.forEach(article => {
      const html = `
        <article>
          <h3>${article.title}</h3>
          <p><a href="${article.url}" target="_blank">Ler mais</a></p>
        </article>
      `;
      topNewsSection.innerHTML += html;
    });
  } catch (err) {
    topNewsSection.innerHTML += "<p>Erro ao carregar Top 3 notícias.</p>";
  }
});

document.getElementById("searchForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const keyword = document.getElementById("searchInput").value.trim();
  if (!keyword) {
    resultsDiv.innerHTML = "<p style='color:#f88'>⚠️ Por favor, insere uma palavra-chave.</p>";
    return;
  }

  resultsDiv.innerHTML = "<p style='color:#ccc'>🔄 A carregar...</p>";

  try {
    const response = await fetch("https://api.spaceflightnewsapi.net/v4/articles");
    const data = await response.json();

    const filtered = data.results.filter(article =>
      article.title.toLowerCase().includes(keyword.toLowerCase())
    );

    if (filtered.length === 0) {
      resultsDiv.innerHTML = "<p style='color:#f88'>❌ Nenhuma notícia encontrada.</p>";
    } else {
      resultsDiv.innerHTML = "";
      filtered.forEach(article => {
        const html = `
          <article>
            <h3>${article.title}</h3>
            <p><a href="${article.url}" target="_blank">Ler mais</a></p>
          </article>
        `;
        resultsDiv.innerHTML += html;
      });
    }
  } catch (error) {
    resultsDiv.innerHTML = "<p>Erro ao carregar notícias.</p>";
    console.error(error);
  }
});

  