numeros = [[], []]
v = 0
for i in range(1, 8):
	v = int(input(f'Digite o {i} valor: '))
	if v % 2 == 0:
		numeros[0].append(v)
	else:
		numeros[1].append(v)
numeros[0].sort()
numeros[1].sort()
print(f'Todos os valores: {numeros}')
print(f'Todos valores pares foram: {numeros[0]}')
print(f'Todos valores impares foram: {numeros[1]}')
