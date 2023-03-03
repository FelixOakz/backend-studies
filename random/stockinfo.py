import requests
import csv


def load_nasdaq_symbols():
    """Load list of nasdaq companies"""
    symbols = {}
    try:
        with open('webstudies/StockChampion/nasdaq_companies.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header row
            for row in reader:
                symbol, name = row
                symbols[symbol] = name

    except Exception as e:
        print("An error occurred while reading the CSV file", e)
        return {}
    return symbols


def lookup(symbol):
    """Look up quote for symbol."""

# contact api
    symbol = symbol.upper().strip()
    api_key = "PFDIMYSMNA5J1BUE"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    try:
        response = requests.get(url)

        # parse response
        stock_data = response.json()
        company_symbol = stock_data["Global Quote"]["01. symbol"]
        closing_price = float(stock_data["Global Quote"]["05. price"])

    except (requests.RequestException, KeyError, TypeError, ValueError):
        return None

    nasdaq_symbols = load_nasdaq_symbols()
    company_name = nasdaq_symbols.get(symbol, "Unknown Company")

    return {
        "name": company_name,
        "price": closing_price,
        "symbol": company_symbol
    }


symbols = [load_nasdaq_symbols()]

for i in range(0, len(symbols)):
    print(f'{symbols[i]}\n')