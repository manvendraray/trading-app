import streamlit as st
import pandas as pd
import yfinance as yt
import plotly.graph_objects as go
import datetime 
import ta 

# --- Page Config ---
st.set_page_config(
    page_title="Stock Analysis",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.markdown(
    """

# Stock Analysis
""",
    unsafe_allow_html=True,
)
st.markdown('---')
# --- 3 Columns ---
col1, col2, col3 = st.columns(3)

today = datetime.date.today()

# --- Inputs ---
with col1:
    ticker = st.text_input("Stock Ticker", "TSLA")

with col2:
    start_date = st.date_input(
        "Choose Start Date",
        datetime.date(today.year - 1, today.month, today.day)
    )

with col3:
    end_date = st.date_input(
        "Choose End Date",
        datetime.date(today.year, today.month, today.day)
    )