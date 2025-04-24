import pyautogui
import time
import pyperclip

# Função para clicar na área de pesquisa, inserir o nome do grupo e entrar no grupo
def entrar_no_grupo(nome_grupo):
    # Clicar na área de pesquisa
    pyautogui.click(220, 149)  # Coordenadas da barra de pesquisa
    time.sleep(2)
    # Inserir o nome do grupo
    pyautogui.typewrite(nome_grupo)
    time.sleep(2)
    # Pressionar Enter para pesquisar o grupo
    pyautogui.press('enter')
    time.sleep(2)
    # Clicar para entrar no grupo
    pyautogui.click(262, 256)  # Coordenadas do botão de entrar no grupo (ajustar conforme necessário)

# Função para enviar uma mensagem no grupo
def enviar_mensagem(mensagem):
    # Clicar na caixa de mensagem
    pyautogui.click(862, 1009)  # Coordenadas da caixa de mensagem (ajustar conforme necessário)
    time.sleep(2)
    # Copiar a mensagem para a área de transferência
    pyperclip.copy(mensagem)
    # Colar a mensagem na caixa de texto
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

# Abrir o WhatsApp (pode variar dependendo do sistema operacional)
pyautogui.press('winleft')
pyautogui.typewrite('WhatsApp')
pyautogui.press('enter')
time.sleep(10)  # Esperar um momento para o WhatsApp abrir

# Nome do grupo
nome_grupo = "Python Avançado - 10794_03/L"

# Entrar no grupo
entrar_no_grupo(nome_grupo)

# Lista de mensagens engraçadas
mensagens = [
    "Por que a vaca foi para o espaço? Para procurar a vaca-nave!",
    "Qual é o mamífero que adora a internet? O mouse!",
    "Por que o pássaro não usa chapéu? Porque ele tem penas na cabeça!",
    "Por que a galinha atravessou a rua? Para chegar ao outro lado!",
    "Qual é o cúmulo da paciência? Plantar uma banana e esperar crescer uma macieira!"
]

# Simular o envio das mensagens
for mensagem in mensagens:
    enviar_mensagem(mensagem)
    time.sleep(2)  # Esperar um pouco entre cada mensagem

# Mensagem de encerramento
enviar_mensagem("Espero que estas piadas tenham alegrado o teu dia! 😄")
