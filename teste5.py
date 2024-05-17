import streamlit as st
import pandas as pd

# Carregar os dados do arquivo CSV
file_path = "Pasta de Yugioh - Página1.csv"
data = pd.read_csv(file_path)

# Exibir gráfico de dispersão
st.scatter_chart(
    data=data,
    x='Raridade',
    y='Preço',
    size='Carta'
)
