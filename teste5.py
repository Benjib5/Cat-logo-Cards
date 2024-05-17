import streamlit as st
import pandas as pd

file_path = "Pasta de Yugioh - Página1.csv"
data = pd.read_csv(file_path)

data.columns = ["Raridade", "Preço"]

data["Carta"] = ['Magro Negro', 'Dragão Negro de Olhos Vermelhos', 'Exodia, "O Proibido"']

st.scatter_chart(
    data=data,
    x='Raridade',
    y='Preço',
    size='Carta'
)
