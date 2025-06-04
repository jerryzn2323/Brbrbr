
def gerar_sugestao(jogo, odds_lista):
    for item in odds_lista:
        if jogo["homeTeam"].lower() in item["home_team"].lower() and jogo["awayTeam"].lower() in item["away_team"].lower():
            try:
                sites = item.get("bookmakers", [])
                if not sites:
                    return "Sem odds disponíveis"
                odds = sites[0]["markets"][0]["outcomes"]
                valores = {x["name"]: x["price"] for x in odds}
                melhor = min(valores, key=valores.get)
                return f"{melhor} (Odd: {valores[melhor]})"
            except:
                return "Erro ao processar odds"
    return "Jogo não encontrado nas odds"
