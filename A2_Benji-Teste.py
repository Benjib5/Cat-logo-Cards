import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def extrair_dados_yugioh(api_url, termo_de_busca):
    # Código de extração de dados

def extrair_dados_pokemon(api_url, termo_de_busca):
    # Código de extração de dados

def criar_grafico(df):
    if df.empty:
        st.write("Nenhum dado disponível para criar o gráfico.")
    else:
        if 'Preço' in df.columns:
            if 'Nome' in df.columns:
                fig, ax = plt.subplots()
                ax.plot(df['Nome'], df['Preço'])
                ax.set_xlabel('Nome')
                ax.set_ylabel('Preço')
                st.pyplot(fig)
            else:
                st.write("Coluna 'Nome' não encontrada no DataFrame.")
        else:
            st.write("Coluna 'Preço' não encontrada no DataFrame.")

def pesquisa_arquivo(api_url, termo_de_busca, extrair_dados_func):
    dados = extrair_dados_func(api_url, termo_de_busca)
    if not dados:
        st.write("Nenhum dado encontrado para o termo de busca.")
    else:
        df = pd.DataFrame(dados)
        st.write(df)
        criar_grafico(df)

st.title('Pesquisa de Cartas')
pesquisa = st.selectbox('Qual o Jogo?', ['Yu-Gi-Oh!', 'Pokémon'])

if pesquisa == 'Yu-Gi-Oh!':
    pesquisa1 = st.text_input('Pesquisa:')
    url_yugioh = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    pesquisa_arquivo(url_yugioh, pesquisa1, extrair_dados_yugioh)
elif pesquisa == 'Pokémon':
    pesquisa2 = st.text_input('Pesquisa:')
    url_pokemon = 'https://api.pokemontcg.io/v2/cards'
    pesquisa_arquivo(url_pokemon, pesquisa2, extrair_dados_pokemon)
else:
    st.write("Opção inválida.")
