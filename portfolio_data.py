import pandas as pd 
import yfinance as yf

def get_portfolio_summary(config_path='portfolio_config.csv'):
    portfolio=pd.read_csv(config_path)['Ticker']
    summary=[]

    for ticker in portfolio:
        stock=yf.Ticker(ticker)
        info=stock.info
        summary.append({
            'Ticker': ticker,
            'Price' : info.get('regularMarketPrice'),
            '52W High' : info.get('fiftyTwoWeekHigh'),
            '52W Low' : info.get('fiftyTwoWeekLow'),
            'PE Ratio' : info.get('trailingPE'),
            'Dividend Yield': info.get('dividendYield'),
            'Market Cap': info.get('marketCap')

        })
    df = pd.DataFrame(summary)
    df.to_csv("data/portfolio_summary.csv", index=False)
    return df
