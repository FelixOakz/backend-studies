entrada = []
pessoas = []
while True:
	entrada.append(str(input('Qual seu nome?: ')))
	entrada.append(str(input('Qual seu peso?: ')))
	if len(pessoas) == 0:
		maior = menor = entrada[1]
	else:
		if entrada[1] > maior:
			maior = entrada[1]
		if entrada[1] < menor:
			menor = entrada[1]
	pessoas.append(entrada[:])
	entrada.clear()
	r = str(input('Deseja continuar? [S/N]: ')).strip()
	if r in 'Nn':
		break
print('-'*40)
print(f'Os dados foram {pessoas}')
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print(f'Maior peso foi de {maior}kg, peso de ', end='')
for i in pessoas:
	if i[1] == maior:
		print(f'{i[0]},', end='')
print()
print(f'Menor peso foi de {menor}kg, peso de ', end='')
for i in pessoas:
	if i[1] == menor:
		print(f'{i[0]},', end='')
print()
