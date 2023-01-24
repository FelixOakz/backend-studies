n = int(input('Type a number to find its factorial: '))
print(f'{n}! Equals = ',end='')
c = n
f = 1
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'Number {n} factorial is: {f}')