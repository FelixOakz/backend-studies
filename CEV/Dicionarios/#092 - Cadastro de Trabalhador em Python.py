import datetime
dict = {}
dict['nome'] = str(input('Qual o nome?: '))
dict['anoNascimento'] = int(input(f'Qual o ano de nascimento de {dict["nome"]}?: '))
age = datetime.date.today().year - dict['anoNascimento']
dict['idade'] = age
dict['numCarteira'] = int(input(f'Qual numero da carteira de trabalho?(0 se nao tem): '))
if dict['numCarteira'] != 0:
	dict['anoContratacao'] = int(input(f'Qual ano de contratacao?: '))
	dict['salario'] = float(input(f'Qual salario?:'))
	dict['aposentadoria'] = dict['idade'] + ((dict['anoContratacao'] + 35) - datetime.date.today().year)
print('-'*30)
for i, j in dict.items():
	print(f'{i} tem o valor {j}.')
