# import + nome da biblioteca 
# from + nome da biblioteca + import + modulo da biblioteca


# Criar e editar um ficheiro txt                         
""" with open("relatorio.txt", "w") as ficheiro:
    ficheiro.write("Relatório de tarefas\n")
    ficheiro.write("=====================\n")
    ficheiro.write("Tarefa aesfew\n") """
    
# import os - operações basicas com ficheiro do sistema
# import shutil  - operações avançadas do sistema ( copiar, mover, fazer backups) 
 
import os
import shutil

# Criar uma nova pasta
os.makedirs("Organizados/Imagens", exist_ok=True)

# Mover ficheiro
shutil.move("foto.jpg", "Organizados/Imagens/foto.jpg")