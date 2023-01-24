import moeda

p = float(input('Type the value: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} equivale a {moeda.dobro(p)}')
print(f'Aumento de 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')