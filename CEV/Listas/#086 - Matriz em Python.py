m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
	for j in range(0, 3):
		m[i][j] = int(input(f'Digite um valor para [{i}, {j}]:'))
for i in range(0, 3):
	for j in range(0, 3):
		print(f'[{m[i][j]:^5}]', end='')
	print()