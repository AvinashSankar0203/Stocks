import requests
import os 
print("config folder exists:", os.path.exists("config/api_keys.py"))
from config.api_keys import ALPHA_VANTAGE_API_KEY

def get_stock_price(ticker):
    url = (
        f"https://www.alphavantage.co/query?"
        f"function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min"
        f"&apikey={ALPHA_VANTAGE_API_KEY}"
    )
    
    response = requests.get(url)
    data = response.json()

    if "Time Series (5min)" not in data:
        return None

    time_series = data["Time Series (5min)"]
    latest_timestamp = list(time_series.keys())[0]
    latest_data = time_series[latest_timestamp]

    return {
        "timestamp": latest_timestamp,
        "open": latest_data["1. open"],
        "high": latest_data["2. high"],
        "low": latest_data["3. low"],
        "close": latest_data["4. close"],
        "volume": latest_data["5. volume"]
    }
