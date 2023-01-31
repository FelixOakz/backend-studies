import yfinance as yf


def lookup(symbol):
    """Look up quote for symbol."""
    symbol.upper().strip()

    ticker = yf.Ticker(symbol)
    todayData = ticker.history(period='1d')
    info = yf.ticker(symbol).info
    price = round(todayData['Close'][0], 2)
    return {
        "name": info['longName'],
        "price": float(price),
        "symbol": symbol
    }

stock = input('enter stock: ')
print(lookup(stock))