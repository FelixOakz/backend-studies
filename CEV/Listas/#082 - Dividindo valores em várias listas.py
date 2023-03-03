lista = []
while True:
	lista.append(int(input('Digite um numero para adicionar a lista: ')))
	r = str(input('deseja continuar? [S/N]')).strip().upper()
	if r == 'N':
		break
par = [x for x in lista if x % 2 == 0]
impar = [x for x in lista if x % 2 != 0]
print(f'A lista completa: {lista}')
print(f'Numeros pares foram {par} e impares foram {impar}')
