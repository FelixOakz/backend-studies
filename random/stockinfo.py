from googlefinance import getQuotes
import json

print json.dumps(getQuotes('tsla'), indent=2)
