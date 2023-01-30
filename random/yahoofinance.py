import yfinance as yf


def lookup(symbol):
    """Look up quote for symbol."""
    symbol.upper().strip()

    if symbol[-1].isdigit():
        symbol = symbol + '.SA'
    try:
        ticker = yf.Ticker(symbol)
        todayData = ticker.history(period='1d')
        return round(todayData['Close'][0], 2)
    except Exception as e:
        return f"Error: Could not retrieve stock data for symbol '{symbol}' - {str(e)}"


stck = input('enter stock: ')
print(lookup(stck))
