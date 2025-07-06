import streamlit as st


st.set_page_config(page_title="Stock Insight Terminal", layout="wide")

st.title("Stock Insight Terminal")

ticker=st.text_input("Enter a stock ticker",value="AAPL")

st.subheader(f" Selected Ticker: {ticker.upper()}")

from core.alpha_vantage_api import get_stock_price
if ticker:
    price_data=get_stock_price(ticker)
    if price_data:
        st.write(f"Price : ${price_data['close']} (as of {price_data['timestamp']})")
    else:
        st.error("Could not fetch stock data")

import os
os.environ["BROWSER_GATHER_USAGE_STATS"] = "false"