def main():
    total = 0
    while True:
        insert = int(input('Insert Coin: '))
        if insert in [5, 10, 25]:
            total += insert
            if total < 50:
                print(f'Amount Due: {50 - total}')
                continue
            else:
                print(f'Change owed: {total - 50}')
                break
        else:
            print(f'Change owed: {50}')

main()
