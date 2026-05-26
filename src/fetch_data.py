import yfinance as yf
from config import TICKERS

def get_data(tickers):
    # Fetch 2 years of adjusted closing prices for a list of ETF tickers
    try:
        data = yf.download(tickers, period='2y', auto_adjust=True)
        return data['Close']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    prices = get_data(TICKERS)
    print(prices)