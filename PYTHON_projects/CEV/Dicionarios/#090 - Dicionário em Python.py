dict = {}
dict['nome'] = str(input('Qual nome?: '))
dict['media'] = float(input(f'Qual a media de {dict["nome"]}?: '))
if dict['media'] >= 7.5:
	dict['situacao'] = 'APROVADO'
elif 4 <= dict['media'] < 7.5:
	dict['situacao'] = 'RECUPERACAO'
else:
	dict['situacao'] = 'REPROVADO'
print('-'*30)
for i, j in dict.items():
	print(f'{i} eh igual a {j}.')
