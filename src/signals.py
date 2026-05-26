import pandas as pd
from fetch_data import get_data
from config import TICKERS

def calculate_momentum(prices):
    # Calculate 3 month momentum for each ETF
    momentum = prices.pct_change(periods=63)
    return momentum.iloc[-1]

def generate_signals(momentum, prices, total_capital):
    # Generate buy/sell/hold signals and calculate momentum weighted share quantities
    signals = pd.Series(index=momentum.index, dtype=str)
    top3 = momentum[momentum > 0].sort_values(ascending=False).index[:3]

    for ticker in momentum.index:
        if momentum[ticker] < 0:
            signals[ticker] = "Sell"
        elif ticker in top3:
            signals[ticker] = "Buy"
        else:
            signals[ticker] = "Hold"

    # Momentum weighted position sizing
    buy_momentum = momentum[signals == "Buy"]
    total_momentum = buy_momentum.sum()
    current_prices = prices.iloc[-1]

    result = pd.DataFrame({
        "Signal": signals,
        "Momentum": momentum,
        "Shares": 0.0
    })

    if total_momentum == 0:
        return result

    for ticker in buy_momentum.index:
        weight = buy_momentum[ticker] / total_momentum
        capital_allocated = weight * total_capital
        result.loc[ticker, "Shares"] = capital_allocated / current_prices[ticker]

    return result

if __name__ == "__main__":
    prices = get_data(TICKERS)
    momentum = calculate_momentum(prices)
    signals = generate_signals(momentum, prices, total_capital=100000) # test value
    print(signals)