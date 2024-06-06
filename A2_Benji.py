import requests
import pandas as pd
import streamlit as st

def extrair_dados_yugioh(api_url, termo_de_busca):
    response = requests.get(api_url)
    if response.status_code != 200:
        st.error(f"Falha ao acessar a API. Status code: {response.status_code}")
        return []

    data = response.json()

    if 'data' not in data:
        st.error("Chave 'data' não encontrada no JSON.")
        return []

    dados = []
    for card in data['data']:
        if termo_de_busca.lower() in card['name'].lower():
            try:
                nome = card['name']
            except KeyError:
                nome = None

            try:
                tipo = card['type']
            except KeyError:
                tipo = None

            try:
                raridade = card['card_sets'][0]['set_rarity']
            except KeyError:
                raridade = None

            try:
                preco = card['card_prices'][0]['cardmarket_price']
            except (KeyError, IndexError):
                preco = None

            dados.append({
                'Nome': nome,
                'Tipo': tipo,
                'Raridade': raridade,
                'Preço': preco
            })
            # st.write(f'Nome: {nome} // Tipo: {tipo} // Raridade: {raridade} // Preço: {preco}')
    return dados

def extrair_dados_pokemon(api_url, termo_de_busca):
    response = requests.get(api_url)
    if response.status_code != 200:
        st.error(f"Falha ao acessar a API. Status code: {response.status_code}")
        return []

    data = response.json()

    if 'data' not in data:
        st.error("Chave 'data' não encontrada no JSON.")
        return []

    dados = []
    for card in data['data']:
        if termo_de_busca.lower() in card['name'].lower():
            try:
                nome = card['name']
            except KeyError:
                nome = None

            try:
                raridade = card['rarity']
            except KeyError:
                raridade = None

            try:
                preco = card['cardmarket']['prices']['averageSellPrice'] if 'cardmarket' in card and 'prices' in card['cardmarket'] else None
            except KeyError:
                preco = None

            dados.append({
                'Nome': nome,
                'Raridade': raridade,
                'Preço': preco
            })
            # st.write(f'Nome: {nome} // Raridade: {raridade} // Preço: {preco}')
    return dados

def pesquisa_arquivo(api_url, termo_de_busca, extrair_dados_func):
    dados = extrair_dados_func(api_url, termo_de_busca)
    if not dados:
        st.warning("Nenhum dado encontrado para o termo de busca.")
    else:
        df = pd.DataFrame(dados)
        df.to_csv('cards.csv', index=False)
        st.dataframe(df)

st.title('Pesquisa de Cartas de TCG')

pesquisa = st.selectbox('Qual o Jogo?', ['Yu-Gi-Oh!', 'Pokémon'])

if pesquisa == 'Yu-Gi-Oh!':
    st.subheader('Yu-Gi-Oh!')
    pesquisa1 = st.text_input('Pesquisa:')
    if st.button('Pesquisar'):
        url_yugioh = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
        pesquisa_arquivo(url_yugioh, pesquisa1, extrair_dados_yugioh)
elif pesquisa == 'Pokémon':
    st.subheader('Pokémon')
    pesquisa2 = st.text_input('Pesquisa:')
    if st.button('Pesquisar'):
        url_pokemon = 'https://api.pokemontcg.io/v2/cards'
        pesquisa_arquivo(url_pokemon, pesquisa2, extrair_dados_pokemon)
