termos = int(input('Quantos termos fibbonaci?: '))
n = 0
nn = 1
nnn = n + nn
cont = 2
print(f'{n} - {nn}', end=' - ')

while cont != termos:
    nnn = n + nn
    print(f'{nnn}', end=" - ")
    n = nn
    nn = nnn
    cont += 1
