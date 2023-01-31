
import requests

def get_stock_data(symbol):
    api_key = "PFDIMYSMNA5J1BUE"
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    stock_data = response.json()
    company_name = stock_data["Global Quote"]["01. symbol"]
    closing_price = float(stock_data["Global Quote"]["05. price"])

    return company_name, closing_price
