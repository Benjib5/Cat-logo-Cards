import streamlit as st
import pandas as pd
import numpy as np
import csv

df=pd.read_csv('Pasta de Yugioh - Página1 (1).csv')

df.plot(kind='line', x='Nome:', y='Preço:', title='Gráfico de linhas do preço das cartas')

df
