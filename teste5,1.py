import csv
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
   {
       "line1,2,3": np."Mago Negro",
       "line4,5,6": np."Dragão Negro de Olhos Vermelhos",
   }
)

st.line_chart(chart_data, x="col1", y="col5")
