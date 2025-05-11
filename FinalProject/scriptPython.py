import requests
import json
from datetime import datetime

url = "https://api.spaceflightnewsapi.net/v4/articles"

def fetch_news():
    response = requests.get(url)
    data = response.json()

    articles = []
    for article in data['results']:
        articles.append({
            "title": article['title'],
            "url": article['url'],
            "publishedAt": article['published_at']
        })

    # Nome do ficheiro com data
    filename = f"noticias_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    print(f"{len(articles)} notícias guardadas em {filename}")

if __name__ == "__main__":
    fetch_news()
