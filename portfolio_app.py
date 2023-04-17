import streamlit as st
import pandas as pd
import plotly.express

st.set_page_config(
    page_title="Main portfolio ",
    page_icon="👋",
)

st.write("Header of portfolio")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
