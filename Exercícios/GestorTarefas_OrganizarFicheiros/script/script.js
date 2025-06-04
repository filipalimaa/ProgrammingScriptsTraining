document.getElementById('adicionarTarefa').addEventListener('click', function() {
    const textoTarefa = document.getElementById('nomeTarefa').value;

    if (textoTarefa.trim() === "") {
        alert("Por favor, insira uma tarefa!");
        return;
    }

    // Criar elemento <li> para a tarefa
    const li = document.createElement('li');
    li.innerText = textoTarefa;

    // Criar botão para remover
    const btnRemover = document.createElement('button');
    btnRemover.innerText = 'X';
    btnRemover.addEventListener('click', function() {
        li.remove();
    });
  
    li.appendChild(btnRemover); 
    document.getElementById('listaTarefas').appendChild(li);

    document.getElementById('nomeTarefa').value = '';
});
