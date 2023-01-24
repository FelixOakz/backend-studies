lista = []
for i in range(0, 5):
	lista.append(int(input(f'Digite um valor para posicao {1}: ')))
print(f'{"-"*30}')
print(f'Lista Digitada: {lista}')
print(f'- O maior numero digitado foi {max(lista)} na posicao {lista.index(max(lista))}')
print(f'- O menor numero digitado foi {min(lista)} na posicao {lista.index(min(lista))}')
