import streamlit as st
import pandas as pd
import numpy as np
import pandas
arquivo_excel = pandas.read_excel('Pasta de Yugioh.xlsx')
arquivo_excel

chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")
