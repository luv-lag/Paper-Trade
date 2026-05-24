import yfinance as yf
import pandas as pd

tickers = ['QQQ' ,'XLK' , 'XLV' , 'SPY' , 'XLI'  , 'XLF' , 'XLE']

def get_data(tickers):

    data = yf.download(tickers , period='2y' , auto_adjust=True)
    print("downloading data...")
    return data['Close']

if __name__ == "__main__":
    print("script started")
    prices = get_data(tickers)
    print(prices)