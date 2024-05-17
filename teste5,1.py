import pandas as pd
import streamlit as st
import csv
from matplotlib import pyplot as plt

st.title("Card Price")

stw = pd.read_csv("Pasta de Yugioh - Página1.csv")

stw_chart = plt.gca()
st.line_chart(stw_chart,str, x=stw.Height, y=stw.Height, width=500, height=500, use_container_width=True)


contact_options = ["Height","Weight"]
contact_selected = st.selectbox("Select a Students value",
                               options = contact_options)


if contact_selected =="Height":
    plt.plot(stw.Name, stw.Height)
    plt.show()
    st.write("result of Height")
else:
    plt.plot(stw.Name, stw.Weight)
    plt.show()
