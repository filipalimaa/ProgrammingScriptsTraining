""" muda ficheiro de sitio"""
import os
import shutil

def organizarArquivos():
    # Diretório de origem (pasta onde os arquivos estão atualmente)
    diretorioOrigem = 'teste2'

    # Diretório de destino (pasta para onde os arquivos serão movidos)
    diretorioDestino = 'teste1'

    # Lista todos os arquivos no diretório de origem
    arquivos = os.listdir(diretorioOrigem)

    # Itera sobre os arquivos e move os arquivos .txt para o diretório de destino
    for arquivo in arquivos:
        if arquivo.endswith('.txt'):
            # Caminho completo do arquivo de origem
            origem = os.path.join(diretorioOrigem, arquivo)
            # Caminho completo do arquivo de destino
            destino = os.path.join(diretorioDestino, arquivo)
            # Move o arquivo para o diretório de destino
            shutil.move(origem, destino)
            print(f'Arquivo {arquivo} movido para {diretorioDestino}')

# Chama a função para organizar os arquivos
organizarArquivos()


"""
import os: O módulo os fornece funções para interagir com o sistema operacional.
Ele é usado neste exemplo para listar os arquivos em um diretório e para 
manipular caminhos de arquivos.

import shutil: O módulo shutil fornece funções de alto nível para 
operações de arquivos. Neste exemplo, é usado para mover os arquivos 
entre diretórios.

def organizar_arquivos():: Esta é uma função definida pelo 
usuário chamada organizar_arquivos. Ela contém uma sequência de comandos que são usados para organizar arquivos de um diretório de origem para um diretório de destino.

diretorio_origem = 'teste2': Esta linha define o 
diretório de origem onde os arquivos estão atualmente. 
Você precisa substituir 'teste2' pelo caminho do diretório real em seu sistema.

diretorio_destino = 'teste1': Esta linha define o 
diretório de destino para onde os arquivos serão movidos. 
Você precisa substituir 'teste1' pelo caminho do diretório real em seu sistema.

arquivos = os.listdir(diretorio_origem): 
Esta linha lista todos os arquivos no diretório de origem e armazena os nomes dos arquivos em uma lista chamada arquivos.

for arquivo in arquivos:: 
Este é um loop for que itera sobre cada arquivo na lista arquivos.

if arquivo.endswith('.txt'):: Este é um condicional que 
verifica se o nome do arquivo termina com a extensão .txt.

origem = os.path.join(diretorio_origem, arquivo): Esta linha cria o 
caminho completo do arquivo de origem combinando o diretório de origem e o nome do arquivo.

destino = os.path.join(diretorio_destino, arquivo): Esta linha cria o caminho 
completo do arquivo de destino combinando o diretório de destino e o nome do arquivo.

shutil.move(origem, destino): Esta linha move o arquivo da origem para o 
destino usando a função shutil.move().

print(f'Arquivo {arquivo} movido para {diretorio_destino}'): 
Esta linha imprime uma mensagem informando que o arquivo foi movido 
com sucesso.

organizar_arquivos(): Esta linha chama a função organizar_arquivos() 
para iniciar o processo de organização de arquivos.
    


"""