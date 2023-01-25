user = input('enter variable: ')
for _ in user:
    if _.isupper():
        print('_' + _.lower(), end='')
    else:
        print(_, end='')
print()
