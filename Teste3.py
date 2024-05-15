!pip install -q matplotlib
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(60)

plt.hist(data, bins=15, color='green', edgecolor='black')

plt.xlabel('N° de Faltas')
plt.ylabel('Frequência')
plt.title('Histórico de Faltas')

plt.show()
st.bar_chart(data)
