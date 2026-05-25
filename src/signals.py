import pandas as pd
from fetch_data import get_data

#Closing prices
tickers = ['QQQ', 'XLK', 'XLV', 'SPY', 'XLI', 'XLF', 'XLE'] #create config file
prices = get_data(tickers)

def calculate_momentum(prices):
    momentum = prices.pct_change(periods = 63)

    return momentum.iloc[-1]

def generate_signals(momentum):
    signals = pd.Series(index=momentum.index, dtype=str)
    top3 = momentum[momentum > 0].sort_values(ascending=False).index[:3]
    
    for ticker in momentum.index:
        if momentum[ticker] < 0:
            signals[ticker] = "Sell"
        elif ticker in top3:
            signals[ticker] = "Buy"
        else:
            signals[ticker] = "Hold"
    
    return signals

if __name__ == "__main__":
    momentum = calculate_momentum(prices)
    signals = generate_signals(momentum)
    print(signals)
