Gestor de Tarefas + Organização de Ficheiros
Objetivo:
Criar uma pequena aplicação web onde o utilizador insere tarefas. As tarefas são guardadas numa lista na interface (HTML/JS). Depois, um script Python organiza automaticamente os ficheiros numa pasta local, como complemento da lógica de produtividade.

 
Passo-a-passo guiado
 
Parte 1 – Interface em HTML + CSS
Objetivo: Criar um formulário simples para inserir tarefas.

Pede aos alunos que:

Criem um ficheiro index.html

Adicionem:

Um <input> para escrever a tarefa

Um <button> para adicionar

Uma <ul> para listar as tarefas

Criem um style.css e liguem ao HTML com <link>

Estilizem o input e o botão com margens e cores básicas

 
Parte 2 – Lógica com JavaScript
Objetivo: Gerir a lista de tarefas no navegador.

Pede aos alunos que:

Criem um ficheiro script.js e liguem ao HTML com <script>

No JS, escrevam:

Um addEventListener para capturar o clique no botão

Validem se o campo está vazio (usar .trim() e .alert())

Criem um novo <li> com o conteúdo da tarefa

Adicionem o <li> à lista (ul) existente

Dica: Usar .appendChild() e .createElement("li")

 
Parte 3 – Automação com Python
Objetivo: Criar um script Python que organiza ficheiros locais, como continuação da lógica de produtividade.

Pede aos alunos que:

Criem um ficheiro organizar_ficheiros.py

Definam uma variável com o nome da pasta (ex: "Downloads")

Listem os ficheiros da pasta com os.listdir()

Verifiquem a extensão de cada ficheiro

Criem subpastas para PDF, imagens, Word, etc.

Movam os ficheiros para a pasta respetiva com shutil.move()

Dica: Criar as pastas automaticamente com os.makedirs(..., exist_ok=True)

 
Bónus (avançado, se houver tempo)
No JS: permitir eliminar uma tarefa com um botão junto ao li

Em Python: gerar um relatório .txt com os ficheiros organizados