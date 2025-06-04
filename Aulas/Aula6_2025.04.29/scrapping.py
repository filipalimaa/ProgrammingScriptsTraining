import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, "html.parser")

frases = soup.find_all("span", class_="text")

for frase in frases:
    print(frase.text)
    
    
lista_frases = [f.text for f in frases]

with open("frases.json", "w", encoding="utf-8") as ficheiro:
    json.dump(lista_frases, ficheiro, ensure_ascii=False, indent=2)
