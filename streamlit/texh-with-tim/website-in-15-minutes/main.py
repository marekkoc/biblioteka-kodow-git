"""
STREAMLIT OVERVIEW


YT channel: Tech with Tim
video: Build a Python Website in 15 Minutes With Streamlit
link: https://www.youtube.com/watch?v=2siBrMsqF44


Created: 2024.11.11
Modyfied: 2024.11.12
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose CSV file", type='csv',)
if uploaded_file: 
    st.write("File uploaded...")

    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.to_list()
    selected_column = st.selectbox("Select the monty to filter by...", columns)
