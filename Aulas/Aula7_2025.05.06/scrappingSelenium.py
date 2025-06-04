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
driver.get("https://quotes.toscrape.com/")

time.sleep(5)
# Localizar todos os elementos <h1>
titulos = driver.find_elements(By.TAG_NAME, "p")

# Imprimir o texto de cada título
for titulo in titulos:
    print(titulo.text)

driver.quit()