import requests
import csv

def load_nasdaq_symbols():
    symbols = {}
    with open('webstudies/trainingTrader/nasdaq_companies.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip the header row
        for row in reader:
            symbol, name = row
            symbols[symbol] = name
    return symbols


def get_company_name(symbol):
    return nasdaq_symbols.get(symbol, "Unknown Company")

def get_stock_data(symbol):
    api_key = "PFDIMYSMNA5J1BUE"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    stock_data = response.json()
    company_name = stock_data["Global Quote"]["01. symbol"]
    closing_price = float(stock_data["Global Quote"]["05. price"])

    return company_name, closing_price, stock_data

nasdaq_symbols = load_nasdaq_symbols()

company_symbol = input("Company Symbol: ").upper().strip()

company_name, closing_price, stock_data = get_stock_data(company_symbol)
print(company_symbol, get_company_name(company_symbol), closing_price)
