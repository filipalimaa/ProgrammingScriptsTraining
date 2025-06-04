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
driver.get("https://www.ipma.pt/pt/otempo/prev.localidade.hora/")

# esperar o carregamento
time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Capturar screenshot
driver.save_screenshot("finalPagina_script.png")

time.sleep(20)
driver.quit()


"""

driver.execute_script()


"""