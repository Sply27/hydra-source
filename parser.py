import json
import requests

URL = "http://127.0.0.1:8000/games.json"

response = requests.get(URL, timeout=20)
response.raise_for_status()

games = response.json()

downloads = []

for game in games:
    downloads.append({
        "title": game["title"],
        "uris": [game["magnet"]],
        "uploadDate": game["uploadDate"],
        "fileSize": game["fileSize"]
    })

source = {
    "name": "My Test Source",
    "downloads": downloads
}

with open("source.json", "w", encoding="utf-8") as file:
    json.dump(source, file, ensure_ascii=False, indent=2)

print(f"Готово! Получено игр: {len(games)}")
input("Нажми Enter для выхода...")