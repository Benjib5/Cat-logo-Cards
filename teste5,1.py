import csv
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
   {
       "col1": np."Nome",
       "col5": np."Preço,
   }
)

st.line_chart(chart_data, x="col1", y="col5")
