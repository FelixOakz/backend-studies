geral = []
temp = []
r = ''
while r in 'Ss':
	temp.append(str(input('Nome: ')))
	temp.append(float(input('Nota 1: ')))
	temp.append(float(input('Nota 2: ')))
	temp.append((temp[1] + temp[2])/2)
	geral.append(temp[:])
	temp.clear()
	r = str(input('Deseja adicionar mais um? [s/n]: '))
print('='*30, 'No.     NOME    MEDIA', '='*30, sep='\n')
for i in range(len(geral)):
	print(f'{i:<5}{geral[i][0]:^10}{geral[i][3]:>5}')
print('-'*30)
while True:
	r = int(input('Mostrar notas de qual aluno? [999 p/ sair]: '))
	if r != 999:
		print(F'>>> As notas de {geral[r][0]} são {geral[r][1]} e {geral[r][2]}')
		print('-' * 30)
	if r == 999:
		print('>>> Programa encerrado.')
		break