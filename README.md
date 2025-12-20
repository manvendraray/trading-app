# Link https://forecasting-time-series.streamlit.app

# 📈 Time-Series Forecasting Dashboard

This project is a **web-based stock analysis and forecasting application** built using **Python and Streamlit**.  
It allows users to explore historical stock data, apply technical indicators, and generate short-term forecasts using classical time-series models.

This project is intended for **learning and analysis**, not financial advice.

---

## 🔍 What does this app do?

The app helps users:

- View historical stock prices
- Analyze trends using technical indicators
- Forecast the next 30 days of closing prices
- Interact with charts and tables in a browser
- Understand model accuracy using simple metrics

Stock data is fetched from **Yahoo Finance**.

---

## 🧠 How does it work? (Pipeline)

Flowchart.png
---

## 📊 Features

### Stock Analysis
- Line and candlestick charts
- Open, High, Low, Close, Volume data
- Technical indicators:
  - Moving Average
  - RSI
  - MACD

### Stock Forecasting
- ARIMA-based time-series forecasting
- 30-day closing price forecast
- Visual comparison of historical and forecasted prices
- Model evaluation using RMSE

### Interactive Dashboard
- Built with Streamlit and Plotly
- User-friendly controls
- Runs directly in the browser

---

## ⚠️ Important Notes

- This project is for **educational purposes only**
- It does **not provide investment advice**
- Forecasts are based only on historical prices
- Some company information may show as **N/A** due to data source limitations

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Plotly
- Pandas & NumPy
- Statsmodels (ARIMA)
- Yahoo Finance (yfinance)

---

## 🚀 How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/your-username/trading-app.git
cd trading-app