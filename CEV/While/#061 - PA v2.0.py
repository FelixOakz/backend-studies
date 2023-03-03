p = int(input('Primeiro termo da PA: '))
r = int(input('Razao da PA: '))
d = p + (r*10)
while p != d:
    print(f'{p}', end=' -> ')
    p += r
print('Fim')


