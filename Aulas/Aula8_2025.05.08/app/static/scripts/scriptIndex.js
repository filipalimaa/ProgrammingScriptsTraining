const searchBtn = document.getElementById('searchBtn');
const searchInput = document.getElementById('search');
const resultsList = document.getElementById('results');
const loadingMsg = document.getElementById('loading');
const errorMsg = document.getElementById('error');
const detailsDiv = document.getElementById('details');
const titleDiv = document.getElementById('title');
const yearDiv = document.getElementById('year');
const typeDiv = document.getElementById('type');
const posterImg = document.getElementById('poster');
const movieActorsDiv= document.getElementById('actors');

searchBtn.addEventListener('click', search);
searchInput.addEventListener('keypress', function(event) {
    // Verifica se a tecla pressionada é "Enter"
    // Se for, chama a função de busca
    if (event.key === 'Enter') {
        search();
    }
});

function search() {
    const searchTerm = searchInput.value.trim();
    if (searchTerm === '') {
        alert('Por favor, insira um termo de pesquisa.');
        return;
    }

    loadingMsg.style.display = 'block';
    errorMsg.style.display = 'none';
    resultsList.innerHTML = '';

        // http://www.omdbapi.com/?i=tt3896198&apikey=4dbc53ec
    fetch(`http://www.omdbapi.com/?s=${searchTerm}&apikey=4dbc53ec`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            loadingMsg.style.display = 'none';
            if (data.Response === 'True') {
                data.Search.forEach(movie => {
                    const li = document.createElement('li');
                    li.textContent = `${movie.Title} (${movie.Year})`;
                    li.dataset.imdbID = movie.imdbID;
                    li.addEventListener('click', () => showDetails(movie.imdbID));
                    resultsList.appendChild(li);
                });
            } else {
                errorMsg.textContent = data.Error;
                errorMsg.style.display = 'block';
            }
        })
        .catch(error => {
            loadingMsg.style.display = 'none';
            errorMsg.textContent = 'Erro ao buscar os dados.';
            errorMsg.style.display = 'block';
        });
}
// Função para mostrar os detalhes do filme

function showDetails(imdbID) {
    fetch(`http://www.omdbapi.com/?i=${imdbID}&apikey=4dbc53ec`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
            titleDiv.textContent = data.Title;
            yearDiv.textContent = `Ano de Lançamento: ${data.Year}`;
            typeDiv.textContent = `Tipo: ${data.Type}`;
            movieActorsDiv.textContent = `Actores: ${data.Actors}`;
            posterImg.src = data.Poster;
            detailsDiv.style.display = 'block';
        })
        .catch(error => console.error('Erro ao procurar detalhes do filme:', error));

}
