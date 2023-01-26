import yfinance as yf


def currentPrice(symbol):
    ticker = yf.Ticker(symbol)
    todayData = ticker.history(period='1d')
    return round(todayData['Close'][0], 2)


stock = input('Enter stock: ').upper().strip()
if stock[-1].isdigit():
    stock = stock + '.SA'

print(f'A share of {stock} costs ${currentPrice(stock)}')
