coins = 0
# accepting input from user and making sure is a positive value, casting to float
while True:
    change = float(input("How much change do I owe you? "))
    if change > 0:
        break

# converting to int
change = round(float(change * 100))
# ammount of coins
coins = change // 25
change %= 25
coins += change // 10
change %= 10
coins += change // 5
change %= 5
coins += change // 1
# print expected result
print(coins)
print('end')