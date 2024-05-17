import streamlit as st
import pandas as pd
import numpy as np
import csv

chart_data = pd.DataFrame(
   {
       "col1": np."Nome",
       "col2": np."Preço",
   }
)

st.line_chart(chart_data, x="col1", y="col2")
