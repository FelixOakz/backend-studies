import yfinance as yf

msft = yf.Ticker("MSFT")
stock = msft.basic_info
print(stock)
