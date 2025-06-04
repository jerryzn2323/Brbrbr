
import requests

API_KEY = "d43448b9bff64b3cbac8c6dfbead664f"

def buscar_jogos(codigo_liga):
    url = f"https://api.football-data.org/v4/competitions/{codigo_liga}/matches?status=SCHEDULED"
    headers = {"X-Auth-Token": API_KEY}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return []
    data = res.json()
    jogos = []
    for match in data.get("matches", []):
        jogos.append({
            "homeTeam": match["homeTeam"]["name"],
            "awayTeam": match["awayTeam"]["name"],
            "status": match["status"]
        })
    return jogos
