import streamlit as st
import pandas as pd
import numpy as np
import csv

chart_data = pd.DataFrame(np.columns=["col1", "col2", "col3"])
      col1 = Pasta de Yugioh - Página1.csv['Raridade']
      col2 = Pasta de Yugioh - Página1.csv['Preço']
chart_data['col4'] = np.(['Magro Negro','Dragão Negro de Olhos Vermelhos','Exodia,"O Proibido"'])

st.scatter_chart(
    chart_data,
    x='col1',
    y='col2',
    card='col4',
    size='col3',
)
