import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('Pasta de Yugioh - Página1 (1).csv')

# Criar a figura e o eixo
fig, ax = plt.subplots()

# Plotar os dados no eixo
df.plot(kind='line', x='Nome:', y='Preço:', ax=ax, title='Gráfico de linhas do preço das cartas')

# Mostrar o gráfico no Streamlit
st.pyplot(fig)
