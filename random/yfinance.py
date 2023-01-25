import yfinance as yf

# Get stock info for Apple Inc.
stock = yf.Ticker("AAPL")
stock_info = stock.info

# Print the current stock price
print(stock_info["regularMarketPrice"])
