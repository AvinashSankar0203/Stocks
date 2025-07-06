import streamlit as st
import pandas as pd
import os
from core.alpha_vantage_api import get_stock_price

# 🚀 Set page config
st.set_page_config(page_title="Stock Insight Terminal", layout="wide")

# 🧠 Sidebar
st.sidebar.title("💼 Stock Insight Terminal")
ticker = st.sidebar.text_input("Enter a stock ticker", value="AAPL")

# 🧱 Main Dashboard
st.title(f"📈 {ticker.upper()} Market Snapshot")

# 🔍 Fetch data
if ticker:
    price_data = get_stock_price(ticker)

    if price_data:
        # 🧊 Columns to mimic Bloomberg layout
        col1, col2 = st.columns([2, 3])

        with col1:
            st.subheader("🔢 Real-Time Metrics")
            st.metric("Current Price", f"${price_data['close']}")
            st.metric("Open", f"${price_data['open']}")
            st.metric("High", f"${price_data['high']}")
            st.metric("Low", f"${price_data['low']}")
            st.metric("Volume", f"{int(float(price_data['volume'])):,}")
            st.caption(f"Last updated: {price_data['timestamp']}")

        with col2:
            st.subheader("📋 Detailed Data Table")
            df = pd.DataFrame([price_data])
            st.dataframe(df, use_container_width=True)

    else:
        st.error("❌ Could not fetch stock data. Please try again later.")
