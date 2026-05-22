# Paper-Trade

**Overview**
A momentum-based paper trading system built in Python. The system fetches historical ETF price data, generates buy/sell signals based on recent price performance, backtests the strategy against historical data and executes simulated trades via the Alpaca API.

**Strategy**
The system uses a momentum strategy: ETFs that have outperformed over a recent lookback period are bought, underperformers are sold. The universe consists of US sector ETFs covering the broad range of the economy.
