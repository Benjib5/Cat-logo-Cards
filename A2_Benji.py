import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Adicionando o código para definir a imagem de fundo
st.markdown(
    """
    <style>
    .stApp {
        background: url('') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Funções de extração de dados
def extrair_dados_yugioh(api_url):
    response = requests.get(api_url)
    if response.status_code != 200:
        st.write(f"Falha ao acessar a API. Status code: {response.status_code}")
        return []

    data = response.json()

    if 'data' not in data:
        st.write("Chave 'data' não encontrada no JSON.")
        return []

    dados = []
    for card in data['data']:
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
    return dados

def extrair_dados_pokemon(api_url):
    response = requests.get(api_url)
    if response.status_code != 200:
        st.write(f"Falha ao acessar a API. Status code: {response.status_code}")
        return []

    data = response.json()

    if 'data' not in data:
        st.write("Chave 'data' não encontrada no JSON.")
        return []

    dados = []
    for card in data['data']:
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
    return dados

def exibir_dados_cartas(dados):
    for carta in dados:
        if st.button(carta['Nome']):
            st.write(f"**Nome:** {carta['Nome']}")
            st.write(f"**Tipo:** {carta.get('Tipo', 'N/A')}")
            st.write(f"**Raridade:** {carta['Raridade']}")
            st.write(f"**Preço:** {carta['Preço']}")

    # Exibir gráfico de barras para os preços
    df = pd.DataFrame(dados)
    if 'Preço' in df.columns:
        plt.figure(figsize=(10, 6))
        df['Preço'] = pd.to_numeric(df['Preço'], errors='coerce')  # Convertendo para números
        df.dropna(subset=['Preço'], inplace=True)  # Removendo valores nulos
        df.plot(kind='bar', x='Nome', y='Preço', color='skyblue')
        plt.title('Preços das Cartas')
        plt.xlabel('Cartas')
        plt.ylabel('Preço')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(plt)

# Interface principal
st.title('Catálogo de Cartas')
pesquisa = st.selectbox('Qual o Jogo?', ['Yu-Gi-Oh!', 'Pokémon'])

if pesquisa == 'Yu-Gi-Oh!':
    url_yugioh = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    dados_yugioh = extrair_dados_yugioh(url_yugioh)
    exibir_dados_cartas(dados_yugioh)
elif pesquisa == 'Pokémon':
    url_pokemon = 'https://api.pokemontcg.io/v2/cards'
    dados_pokemon = extrair_dados_pokemon(url_pokemon)
    exibir_dados_cartas(dados_pokemon)
else:
    st.write("Opção inválida.")
