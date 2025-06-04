from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chromePath = Service(r"C:\AULAS\aulasScript\aula7\selenium\chromedriver.exe")
# abrir o ChromeDriver
driver = webdriver.Chrome(service=chromePath)

# ir para uma página 
driver.get("https://www.google.com")

# esperar o carregamento
time.sleep(10000000)

# imprimir o titulo da página
print(driver.title)



time.sleep(5)

#fechar o browser
driver.quit()