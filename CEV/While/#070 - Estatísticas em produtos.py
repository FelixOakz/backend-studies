tot = valormil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o produto: '))
    preco = int(input('Digite o valor do produto [R$]: '))
    cont += 1
    tot += preco
    if preco > 1000:
        valormil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\n- - - Resumo da Compra - - -')
print(f'O total da compra foi de R${tot:.2f}')
print(f'Temos {valormil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor}')
