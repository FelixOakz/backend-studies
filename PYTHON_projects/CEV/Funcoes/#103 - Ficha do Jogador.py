def ficha(nome, gols=0):
	print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


nome = str(input('Nome do jogador?: '))
gols = input('Numero de gols?: ')
if nome == '':
	ficha('Desconhecido', gols)
else:
	if gols.isnumeric():
		ficha(nome, gols)
	else:
		ficha(nome)
