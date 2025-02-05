"""
STREAMLIT OVERVIEW


YT channel: Tech with Tim
video: Build a Python Website in 15 Minutes With Streamlit
link: https://www.youtube.com/watch?v=2siBrMsqF44


Created: 2024.11.11
Modyfied: 2024.11.13
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose CSV file", type='csv',)
if uploaded_file: 
    st.write("File uploaded...")

    df = pd.read_csv(uploaded_file, index_col=0, decimal='.')    
    df['rok'] = df['rok'].astype(str)
    #df['rok'] = df['rok'].astype(int)

    for c in df.columns[1:]: 
        df.style.format({ c: '{:.2f}'})
    #df.style.format({"rok":'i'})
   

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    year = df['rok'].unique()
    selected_column = st.selectbox("Select a year...", year)

    df_year = df[df['rok'] == selected_column]
    st.write(df_year)

    select_month = st.selectbox("Select a month...", df.columns[1:])
    
    st.subheader("Plot selected month weight in the year")

    x_axis = list(range(1, 31))
        
    if st.button("Generate plot"):
        st.line_chart(df_year[select_month]) 
    
else:
    st.write("Waiting on file upload...")


    
