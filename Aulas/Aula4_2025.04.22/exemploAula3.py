"abrir o browser e pesquisar por algo"

import pyautogui
import subprocess
import time

def openChrome():
    # Caminho completo para o executável do Chrome
    chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    # Abre o navegador Chrome
    subprocess.Popen([chromePath])

def searchGoogle(term):
    # Move o mouse para a barra de endereço do navegador
    pyautogui.moveTo(50, 50, duration=0.5)
    pyautogui.click()

    # Digita o termo de pesquisa
    pyautogui.typewrite(term, interval=0.1)

    # Pressiona a tecla "Enter" para realizar a pesquisa
    pyautogui.press("enter")

def main():
    # Espera 5 segundos antes de começar para dar tempo de abrir o navegador
    time.sleep(5)

    openChrome()

    # Espera o Chrome abrir
    time.sleep(10)

    # Termo a ser pesquisado
    searchTerm = "Python"

    searchGoogle(searchTerm)

if __name__ == "__main__":
    main()

"""
import pyautogui: Importa a biblioteca PyAutoGUI, que permite automatizar 
a interação com o mouse e o teclado.

import subprocess: Importa o módulo subprocess, que é usado para criar 
processos e interagir com programas externos.

import time: Importa o módulo time, que fornece funções para trabalhar 
com o tempo.

def openChrome():: Define uma função chamada openChrome() que 
será usada para abrir o navegador Chrome.

chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe": 
Define o caminho completo para o executável do Google Chrome.

subprocess.Popen([chromePath]): Abre o navegador Chrome usando a 
função subprocess.Popen() e passando o caminho do executável como argumento.

def searchGoogle(term):: Define uma função chamada searchGoogle(term) 
que será usada para pesquisar no Google.

pyautogui.moveTo(50, 50, duration=0.5): Move o mouse para as coordenadas 
(50, 50) na tela com uma duração de 0.5 segundos.

pyautogui.click(): Simula um clique do mouse, que coloca o 
foco na barra de endereço do navegador.

pyautogui.typewrite(term, interval=0.1): Digita o termo de pesquisa 
especificado com um intervalo de 0.1 segundo entre cada caractere.

pyautogui.press("enter"): Simula pressionar a tecla "Enter" 
para realizar a pesquisa.

def main():: Define uma função principal chamada main().

time.sleep(5): Espera 5 segundos antes de começar para dar 
tempo de abrir o navegador.

openChrome(): Chama a função openChrome() para abrir o navegador Chrome.

time.sleep(10): Espera 10 segundos para o navegador abrir completamente.

searchTerm = "Python": Define o termo de pesquisa como "Python".

searchGoogle(searchTerm): Chama a função searchGoogle() para pesquisar 
pelo termo definido.

if __name__ == "__main__": main(): Verifica se o script está sendo 
executado diretamente e, nesse caso, chama a função main().

"""