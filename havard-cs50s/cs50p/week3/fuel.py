def main():
    value = fuel_percent("Enter gauge fraction: ")
    if value <= 1:
        print('E')
    elif value >= 99:
        print('F')
    else:
        print(f'{round(value)}%')


def fuel_percent(value):
    while True:
        try:
            x, y = map(int, input(value).split('/'))
            if x <= y:
                z = (x / y) * 100
                return z
        except (ValueError, ZeroDivisionError):
            pass


main()
