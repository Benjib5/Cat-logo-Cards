import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def extrair_dados_yugioh(api_url, termo_de_busca):
    # Código de extração de dados

def extrair_dados_pokemon(api_url, termo_de_busca):
    # Código de extração de dados

def pesquisa_arquivo(api_url, termo_de_busca, extrair_dados_func):
    # Código de pesquisa

st.title('Pesquisa de Cartas')
pesquisa = st.selectbox('Qual o Jogo?', ['Yu-Gi-Oh!', 'Pokémon'])

if pesquisa == 'Yu-Gi-Oh!':
    pesquisa1 = st.text_input('Pesquisa:')
    url_yugioh = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    dados = extrair_dados_yugioh(url_yugioh, pesquisa1)
    if dados:
        df = pd.DataFrame(dados)
        st.write(df)
        # Exemplo de gráfico de linha com Matplotlib
        fig, ax = plt.subplots()
        ax.plot(df['Nome'], df['Preço'])
        ax.set_xlabel('Nome')
        ax.set_ylabel('Preço')
        st.pyplot(fig)
elif pesquisa == 'Pokémon':
    pesquisa2 = st.text_input('Pesquisa:')
    url_pokemon = 'https://api.pokemontcg.io/v2/cards'
    dados = extrair_dados_pokemon(url_pokemon, pesquisa2)
    if dados:
        df = pd.DataFrame(dados)
        st.write(df)
        # Exemplo de gráfico de linha com Plotly
        fig = px.line(df, x='Nome', y='Preço', title='Preço das Cartas Pokémon')
        st.plotly_chart(fig)
else:
    st.write("Opção inválida.")
