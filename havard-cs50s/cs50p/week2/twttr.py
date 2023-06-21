stdin = input('Input: ')
letters = 'A,E,I,O,U,a,e,i,o,u'
for i in stdin:
    if i in letters:
        print('', end='')
    else:
        print(i, end='')
print()
# other try?