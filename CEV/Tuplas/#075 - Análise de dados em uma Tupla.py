tuple = ()
par = 0
for val in range(1, 5):
	num = int(input(f'qual o {val} valor? '))
	tuple = tuple + (num,)
	if num % 2 == 0:
		par += 1
print(f'O valor 9 apareceu {tuple.count(9)} vezes.')
if 3 in tuple:
	print(f'O valor 3 foi digitado na posicao {tuple.index(3)+1}')
else:
	print('O valor 3 nao foi digitado.')
print(f'Apareceram {par} numeros pares.')