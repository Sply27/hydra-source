import json
import requests
from datetime import datetime, timezone

# URL источника с разрешёнными данными
SOURCE_URL = "https://example.com/games.json"

# Имя нашего Hydra-источника
SOURCE_NAME = "My Hydra Source"

try:
    response = requests.get(
        SOURCE_URL,
        timeout=30,
        headers={
            "User-Agent": "HydraSourceUpdater/1.0"
        }
    )

    response.raise_for_status()
    games = response.json()

    downloads = []

    for game in games:
        downloads.append({
            "title": game["title"],
            "uris": [game["uri"]],
            "uploadDate": game.get(
                "uploadDate",
                datetime.now(timezone.utc).isoformat()
            ),
            "fileSize": game.get("fileSize", "Unknown")
        })

    source = {
        "name": SOURCE_NAME,
        "downloads": downloads
    }

    with open("source.json", "w", encoding="utf-8") as file:
        json.dump(
            source,
            file,
            ensure_ascii=False,
            indent=2
        )

    print(f"Готово! Получено записей: {len(downloads)}")
    print("source.json обновлён.")

except Exception as error:
    print("ОШИБКА:")
    print(error)

input("Нажми Enter для выхода...")