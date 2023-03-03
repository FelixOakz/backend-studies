lista = []
while True:
	lista.append(int(input('Digite um valor: ')))
	r = str(input('Deseja continuar? [S/N]: '))
	if r in 'nN':
		break
lista.sort(reverse=True)
print(f'A lista tem {len(lista)} digitos.')
print(f'Lista em ordem reversa: {lista}')
if 5 in lista:
	print('O valor 5 faz parte da lista!')
else:
	print('O valor 5 nao foi encontrado na lista!')
