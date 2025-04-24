""" Abre um ficheiro notepad escreve algo e fecha-o"""

import pyautogui
import time
import subprocess
import os

def salvarEFechar():
    # Salva o arquivo
    pyautogui.hotkey('ctrl', 's')
    # Aguarda um momento para o diálogo de salvar abrir
    time.sleep(1)
    # Digita o nome do arquivo
    pyautogui.write('mensagem.txt')
    # Pressiona Enter para confirmar o nome do arquivo
    pyautogui.press('enter')
    print("Arquivo salvo automaticamente.")
    # Aguarda um momento para o arquivo ser salvo completamente
    time.sleep(1)
    # Fecha o Bloco de Notas
    pyautogui.hotkey('alt', 'f4')

# Abre o Bloco de Notas
subprocess.Popen(['notepad.exe'])

# Aguarda um momento para o Bloco de Notas abrir
time.sleep(2)

# Escreve uma mensagem
pyautogui.write('Ola, mundo!')

# Salva, fecha o Bloco de Notas e encerra o processo
salvarEFechar()



"""
import pyautogui: PyAutoGUI é uma biblioteca Python que permite automatizar
interações com o mouse e o teclado. Ele é usado aqui para controlar a 
 interface do usuário do Bloco de Notas.

import time: O módulo time fornece funções para trabalhar com o tempo. 
É usado aqui para adicionar atrasos entre as diferentes etapas da automação.

import subprocess: O módulo subprocess permite criar novos processos, 
conectar-se a seus tubos de entrada/saída/erro e obter seus códigos de saída. 
Neste caso, estamos usando-o para abrir o Bloco de Notas.

import os: O módulo os fornece uma maneira de usar funcionalidades 
dependentes de sistema operacional. Neste exemplo, não é usado explicitamente, 
mas geralmente é útil para lidar com caminhos de arquivos e outras operações 
relacionadas ao sistema operacional.

def salvar_e_fechar():: Esta é uma função definida pelo usuário chamada 
salvar_e_fechar. Ela contém uma sequência de comandos que são usados 
para salvar um arquivo no Bloco de Notas e fechá-lo.

subprocess.Popen(['notepad.exe']): Esta linha abre o Bloco de Notas 
usando o módulo subprocess.
subprocess.Popen é uma função em Python que é usada para iniciar 
novos processos. 
Ela é uma parte do módulo subprocess, que fornece uma maneira de interagir 
com programas externos em Python.


time.sleep(2): Isso faz o programa esperar por 2 segundos antes de continuar. 
Isso é útil para garantir que o Bloco de Notas tenha tempo suficiente para 
ser aberto antes de prosseguir.

pyautogui.write('Ola, mundo!'): Isso escreve a mensagem "Olá, mundo!" no 
Bloco de Notas usando o PyAutoGUI.

salvar_e_fechar(): Isso chama a função salvar_e_fechar, que salva o 
arquivo no Bloco de Notas e o fecha.
    """