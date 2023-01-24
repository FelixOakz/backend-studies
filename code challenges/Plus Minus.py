arr = input('enter array: ').strip()

def plusMinus(arr, n):
    pos = neg = zer = 0
    for num in arr:
        if num < 0:
            neg += 1
        elif num == 0:
            zer += 1
        elif num > 0:
            pos += 1
    print(f'{pos/n:.6f}')
    print(f'{neg/n:.6f}')
    print(f'{zer/n:.6f}')