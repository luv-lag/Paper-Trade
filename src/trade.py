import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from signals import generate_signals, calculate_momentum
from fetch_data import get_data
from config import TICKERS

# Load API keys
load_dotenv()
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")

# Connect to Alpaca paper trading
client = TradingClient(API_KEY, API_SECRET, paper=True)

def is_market_open():
    # Check if the US market is currently open
    clock = client.get_clock()
    return clock.is_open

def execute_trades(signals):
    # Execute buy/sell orders on Alpaca based on momentum signals
    for ticker, row in signals.iterrows():
        try:
            if row["Signal"] == "Buy":
                qty = round(row["Shares"])
                if qty < 1:
                    print(f"Skipping {ticker}, position size too small")
                    continue
                order = MarketOrderRequest(
                    symbol=ticker,
                    qty=qty,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                )
                client.submit_order(order)
                print(f"Bought {qty} shares of {ticker}")

            elif row["Signal"] == "Sell":
                try:
                    position = client.get_open_position(ticker)
                    qty_held = float(position.qty)
                    if qty_held > 0:
                        order = MarketOrderRequest(
                            symbol=ticker,
                            qty=qty_held,
                            side=OrderSide.SELL,
                            time_in_force=TimeInForce.DAY
                        )
                        client.submit_order(order)
                        print(f"Sold {qty_held} shares of {ticker}")
                except Exception:
                    print(f"No position in {ticker}, skipping sell")

            else:
                print(f"Holding {ticker}")

        except Exception as e:
            print(f"Error trading {ticker}: {e}")

if __name__ == "__main__":
    prices = get_data(TICKERS)
    momentum = calculate_momentum(prices)

    # Fetch real portfolio value from Alpaca
    account = client.get_account()
    total_capital = float(account.portfolio_value)
    print(f"Portfolio value: ${total_capital:,.2f}")

    signals = generate_signals(momentum, prices, total_capital)
    print(signals)

    if is_market_open():
        execute_trades(signals)
    else:
        print("Market is closed, no trades executed")