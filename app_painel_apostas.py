
import streamlit as st
from jogos_api import buscar_jogos
from odds_api import buscar_odds
from regras_aposta import gerar_sugestao

st.set_page_config(layout="wide")
st.title("⚽ Painel Inteligente de Apostas Esportivas")

st.sidebar.title("🔍 Filtros")
ligas = {
    "Brasileirão (BSA)": "BSA",
    "Premier League (PL)": "PL",
    "La Liga (PD)": "PD",
    "Serie A Italiana (SA)": "SA",
    "Bundesliga (BL1)": "BL1",
    "Ligue 1 Francesa (FL1)": "FL1"
}
liga_nome = st.sidebar.selectbox("Liga", list(ligas.keys()))
liga_codigo = ligas[liga_nome]

st.info(f"Carregando jogos da liga: {liga_nome}")

jogos = buscar_jogos(liga_codigo)
odds = buscar_odds("soccer", region="uk")

if not jogos:
    st.warning("Nenhum jogo encontrado para a liga selecionada.")
    st.markdown("Verifique se a temporada está em andamento.")
else:
    st.markdown(f"### Jogos encontrados: {len(jogos)}")
    for jogo in jogos:
        st.subheader(f"⚽ {jogo['homeTeam']} x {jogo['awayTeam']}")
        st.write(f"Status: {jogo['status']}")
        sug = gerar_sugestao(jogo, odds)
        st.success(f"📌 Sugestão de aposta: **{sug}**")
        st.markdown("---")
