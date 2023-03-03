lista = []
while True:
	n = int(input('Digite um numero: '))
	if n not in lista:
		lista.append(n)
		print('Valor adicionado com sucesso.')
	else:
		print('Valor duplicado')
	r = str(input('Quer continuar?'))
	if r in 'nN':
		break
lista.sort()
print(lista)
