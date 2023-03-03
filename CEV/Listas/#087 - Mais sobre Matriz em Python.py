m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = col3 = 0
for i in range(3):
	for j in range(3):
		m[i][j] = int(input(f'Digite um valor para [{i}, {j}]:'))
		par += m[i][j] if m[i][j] % 2 == 0 else 0
		col3 += m[i][j] if j == 2 else 0
print('-'* 35, *m,'-'* 35, sep='\n')
print(f'A soma dos valores pares eh {par}.')
print(f'A soma dos valores da terceira coluna eh de {col3}.')
print(f'O maior valor da segunda linha eh {max(m[1])}.')
