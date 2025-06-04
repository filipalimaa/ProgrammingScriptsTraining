from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromePath = Service(r"C:\AULAS\aulasScript\aula7\selenium\chromedriver.exe")
# abrir o ChromeDriver
driver = webdriver.Chrome(service=chromePath)

# ir para uma página 
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")

# esperar o carregamento
time.sleep(5)

iframe = driver.find_element(By.ID, "iframeResult")
driver.switch_to.frame(iframe)

# Preencher o formulário
nome = driver.find_element(By.NAME, "fname")
nome.clear()  # Limpar o campo
nome.send_keys("João")

sobrenome = driver.find_element(By.NAME, "lname")
sobrenome.clear()
sobrenome.send_keys("Silva")

# Clicar no botão de enviar
botao = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
botao.click()

# Esperar a mensagem de confirmação
mensagem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "p"))
)
print("Mensagem:", mensagem.text)

# Capturar screenshot
driver.save_screenshot("formulario_concluido.png")

# Voltar ao contexto principal
driver.switch_to.default_content()
driver.quit()


"""

driver.execute_script()


"""