import streamlit as st
import plotly.graph_objects as go
from data_fetcher import get_stock_data
from indicators import add_indicators
from signal_engine import generate_signal
from risk_manager import calculate_levels

st.set_page_config(layout="wide")
st.title("📊 TradeVision AI – India & US Stock Signals")

market = st.sidebar.selectbox("Market", ["India", "US"])

if market == "India":
    symbol = st.sidebar.text_input("Stock Symbol", "RELIANCE.NS")
else:
    symbol = st.sidebar.text_input("Stock Symbol", "AAPL")

interval = st.sidebar.selectbox("Timeframe", ["1d", "1h", "15m"])

df = get_stock_data(symbol, interval=interval)
df = add_indicators(df)

signal, confidence = generate_signal(df)
price = df['Close'].iloc[-1]
sl, target = calculate_levels(price, signal)

col1, col2 = st.columns([3,1])

with col1:
    fig = go.Figure()
    fig.add_candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )
    fig.add_scatter(x=df.index, y=df['EMA20'], name="EMA20")
    fig.add_scatter(x=df.index, y=df['EMA50'], name="EMA50")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📌 Upcoming Position")
    st.metric("Signal", signal)
    st.metric("Confidence", f"{confidence}%")
    st.metric("Entry", round(price,2))
    st.metric("Stop Loss", sl)
    st.metric("Target", target)

st.caption("⚠️ Educational purpose only. Not financial advice.")
