from stockinfo import lookup

portifolio = [{'symbol': 'AAPL', 'shares': 7, 'price': 151.73}, {'symbol': 'AMZN', 'shares': 3, 'price': 0.0}, {'symbol': 'MSFT',
                                                                                                                'shares': 4, 'price': 256.77}, {'symbol': 'NFLX', 'shares': 3, 'price': 361.48}, {'symbol': 'TSLA', 'shares': 5, 'price': 194.76}]

print('Before:')
for p in portifolio:
    print(p)

for i in range(0, len(portifolio)):
    currentValue = lookup(portifolio[i]["symbol"])
    portifolio[i].update(currentValue)

print('AFTER:')
for p in portifolio:
    print(p)
