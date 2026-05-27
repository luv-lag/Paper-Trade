import pandas as pd
import numpy as np
import matplotlib.pylot as plt 
import matplotlib.dates as mdates
from fetch_data import get_data
from config import TICKERS



LOOKBACK = 63    #following signals.py
REBALANCE_FREQ = 21 #trading balance
TOP_N = 3 # num of etfs
total_capital = 100
def run_backtest(prices, lookback = LOOKBACK, rebalnce_freq = REBLANCE_FREQ, top_n = TOP_N):
  portfolio_values = []
  dates = []
  start_idx = lookback
  cash = TOTAL_CAPITAL
  holdings = []
  rebalance_dates = range(start_idx, len(prices), rebalance_freq)
  for i in range (start_idx, len(prices)):
    current_prices = prices.iloc[i]
    if i in rebalance_dates:
      for ticker, shares in holdings.items():
        if ticker in current_prices and not np.isnan(current_prices[ticker]):
          cash += shares * current_price
        holding = {}
        window = prices.iloc [i - lookback:i]
        momentum = (window.iloc [-1] -window.iloc[0]) / window.iloc[0]
        positive = momentum[monentum > 0].sort_values(ascending=False)
        top_picks = positive.head(topn)
        if not top_picks.empty:
          total_momentum = top_picks.sum()
          for ticker , mom in top_picks.items():
            weight = mom /total_momentum
            allocated = weight * cash
            price = current_price.get(ticker, np.nan)
            if not np.isnan(price) and price > 0:
              shares = allocated / price
              holdings[ticker] = shares
              cash -= shares * price   
    portfolio_value = cash
        for ticker, shares in holdings.items():
            price = current_prices.get(ticker, np.nan)
            if not np.isnan(price):
                portfolio_value += shares * price
 
        portfolio_values.append(portfolio_value)
        dates.append(prices.index[i])
 
    return pd.Series(portfolio_values, index=dates, name="Portfolio Value")
 
 
def compute_metrics(portfolio: pd.Series, prices: pd.DataFrame, benchmark_ticker="SPY"):
            
