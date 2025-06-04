
import requests

ODDS_KEY = "62aae1245080935be30ac333264dca60"

def buscar_odds(sport, region="uk"):
    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={ODDS_KEY}&regions={region}&markets=h2h"
    res = requests.get(url)
    if res.status_code != 200:
        return []
    return res.json()
