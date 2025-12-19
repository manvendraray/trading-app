import datetime
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import ta
import yfinance as yf

from pages.utils.plotly_figure import (
    plotly_table,
    close_chart,
    candlestick,
    Moving_average,
    RSI,
    MACD,
)

# =========================
# Page config & title
# =========================
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="📊",
    layout="wide",
)

st.markdown("# 📊 Stock Analysis")
st.markdown("---")

today = datetime.date.today()

# =========================
# Popular tickers & inputs
# =========================
popular_stocks = {
    "NVIDIA (NVDA)": "NVDA",
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Tesla (TSLA)": "TSLA",
    "Amazon (AMZN)": "AMZN",
    "Meta (META)": "META",
    "Google / Alphabet (GOOGL)": "GOOGL",
    "Netflix (NFLX)": "NFLX",
}

col1, col2, col3 = st.columns(3)

with col1:
    mode = st.radio(
        "How do you want to choose?",
        ["Popular list", "Type manually"],
        horizontal=True,
    )

    if mode == "Popular list":
        stock_label = st.selectbox("Choose a stock", list(popular_stocks.keys()))
        ticker = popular_stocks[stock_label]
    else:
        ticker = st.text_input("Stock Ticker", "TSLA")

with col2:
    start_date = st.date_input(
        "Choose Start Date",
        datetime.date(today.year - 1, today.month, today.day),
    )

with col3:
    end_date = st.date_input(
        "Choose End Date",
        datetime.date(today.year, today.month, today.day),
    )

st.subheader(ticker)

# =========================
# Company info (SAFE)
# =========================
stock = yf.Ticker(ticker)

try:
    stock_info = stock.info
except Exception:
    stock_info = {}

stock_name = stock_label if mode == "Popular list" else stock_info.get("longName", ticker)

# ---------- Sidebar ----------
logo_url = stock_info.get("logo_url")
if logo_url:
    st.sidebar.image(logo_url, width=200)

st.sidebar.markdown(f"# {stock_name}")
st.sidebar.markdown(f"**Ticker:** `{ticker}`")

sector = stock_info.get("sector")
if sector:
    st.sidebar.markdown(f"**Sector:** {sector}")

employees = stock_info.get("fullTimeEmployees")
if employees:
    st.sidebar.markdown(f"**Employees:** {employees:,}")

website = stock_info.get("website")
if website:
    st.sidebar.markdown(f"**Website:** [{website}]({website})")

summary = stock_info.get("longBusinessSummary", "")
if summary:
    st.sidebar.markdown("### About")
    st.sidebar.markdown(summary[:500] + ("..." if len(summary) > 500 else ""))

st.sidebar.markdown("---")
st.sidebar.write("Developed by Manvendra Ray")
st.sidebar.write("Contact: mr6695@nyu.edu")

# =========================
# Fundamentals tables (SAFE)
# =========================
col1, col2 = st.columns(2)

with col1:
    df_left = pd.DataFrame(
        {
            "Metric": ["Market Cap", "Beta", "EPS", "PE Ratio"],
            "Value": [
                stock_info.get("marketCap", "N/A"),
                stock_info.get("beta", "N/A"),
                stock_info.get("trailingEps", "N/A"),
                stock_info.get("trailingPE", "N/A"),
            ],
        }
    )
    st.dataframe(df_left, hide_index=True, use_container_width=True)

with col2:
    df_right = pd.DataFrame(
        {
            "Metric": [
                "Quick Ratio",
                "Revenue per Share",
                "Profit Margins",
                "Debt to Equity",
                "Return on Equity",
            ],
            "Value": [
                stock_info.get("quickRatio", "N/A"),
                stock_info.get("revenuePerShare", "N/A"),
                stock_info.get("profitMargins", "N/A"),
                stock_info.get("debtToEquity", "N/A"),
                stock_info.get("returnOnEquity", "N/A"),
            ],
        }
    )
    st.dataframe(df_right, hide_index=True, use_container_width=True)

st.caption("Some company fundamentals may be temporarily unavailable.")

# =========================
# Historical price data
# =========================
data = yf.download(ticker, start=start_date, end=end_date)

df_select = data[["Open", "High", "Low", "Close", "Volume"]].copy()
if isinstance(df_select.columns, pd.MultiIndex):
    df_select.columns = df_select.columns.get_level_values(0)

# =========================
# Metrics
# =========================
col1, col2, col3 = st.columns(3)

last_close = float(data["Close"].iloc[-1])
prev_close = float(data["Close"].iloc[-2])
daily_change = last_close - prev_close

col1.metric("Last Close", round(last_close, 2), round(daily_change, 2))

# =========================
# Last 10 days
# =========================
last_10_df = data.tail(10).sort_index(ascending=False).round(3)
if isinstance(last_10_df.columns, pd.MultiIndex):
    last_10_df.columns = last_10_df.columns.get_level_values(0)

history_df = last_10_df.reset_index().rename(columns={"index": "Date"})

st.write("##### Historical Data (Last 10 Days)")
st.dataframe(history_df, hide_index=True, use_container_width=True)

# =========================
# Time period buttons
# =========================
cols = st.columns(7)
labels = ["5D", "1M", "6M", "YTD", "1Y", "5Y", "MAX"]
values = ["5d", "1mo", "6mo", "ytd", "1y", "5y", "max"]

num_period = ""
for c, label, val in zip(cols, labels, values):
    with c:
        if st.button(label):
            num_period = val

if num_period == "":
    num_period = "1y"

# =========================
# Chart selection
# =========================
col1, col2, col3 = st.columns([1, 1, 4])

with col1:
    chart_type = st.selectbox("", ("Candle", "Line"))

with col2:
    indicators = st.selectbox(
        "",
        ("RSI", "MACD") if chart_type == "Candle" else ("RSI", "Moving Average", "MACD"),
    )

ticker_ = yf.Ticker(ticker)
data1 = ticker_.history(period="max")

# =========================
# Charts
# =========================
if chart_type == "Candle":
    st.plotly_chart(candlestick(data1, num_period), use_container_width=True)
else:
    st.plotly_chart(close_chart(data1, num_period), use_container_width=True)

if indicators == "RSI":
    st.plotly_chart(RSI(data1, num_period), use_container_width=True)
elif indicators == "MACD":
    st.plotly_chart(MACD(data1, num_period), use_container_width=True)
elif indicators == "Moving Average":
    st.plotly_chart(Moving_average(data1, num_period), use_container_width=True)

# =========================
# Built-in charts
# =========================
st.subheader("Open & Close Prices")
st.line_chart(df_select[["Open", "Close"]])

st.subheader("High & Low Prices")
st.line_chart(df_select[["High", "Low"]])

st.subheader("Volume")
st.bar_chart(df_select["Volume"])

st.subheader("Moving Averages")
moveavg_len = st.slider("Moving average window", 1, 250, 50)
st.line_chart(df_select[["Open", "Close"]].rolling(moveavg_len).mean())
