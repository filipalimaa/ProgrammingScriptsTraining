import os
import shutil

nomePasta = r"C:\Users\filipa.lima\Documents\ProgrammingScriptsTraining\Exercícios\GestorTarefas_OrganizarFicheiros"

arquivos = os.listdir(nomePasta)

extensions = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Texto": [".txt"],
    "Python": [".py"],
    "JavaScript": [".js"],
    "HTML": [".html", ".css"]
}

for file in arquivos:
    path = os.path.join(nomePasta, file)
    
    if os.path.isdir(path):
        continue
    
    categoria, extension = os.path.splitext(file)
    
    for allExtensions, extencoes in extensions.items():
        if extension.lower() in extencoes:
            newFolder = os.path.join(nomePasta, categoria)
            os.makedirs(newFolder, exist_ok=True)
            newPath = os.path.join(newFolder, file)
            shutil.move(path, newPath)
            print(f"Movido {file} -> {categoria}")