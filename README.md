# Paper-Trade
**Overview**
A momentum-based paper trading system built in Python. The system fetches historical ETF price data, generates buy/sell signals based on recent price performance, backtests the strategy against historical data and executes simulated trades via the Alpaca API.
This project serves as the foundational layer for a more advanced language model driven trading system that will incorporate sentiment analysis, web scraping and contrarian philosophy into its signals.
**Strategy**
The system uses a momentum strategy — ETFs that have outperformed over a recent lookback period are bought, underperformers are sold. The universe consists of US sector ETFs covering a broad range of the economy.
