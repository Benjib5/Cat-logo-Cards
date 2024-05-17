import streamlit as st
import pandas as pd
import numpy as np
import csv

chart_data = pd.DataFrame(columns=["col1", "col5"])

st.line_chart(
   chart_data, x="col1", y=["col2"], color=["#FF0000", "#0000FF"]
)
