# bugado, mostra a mesma quantidade de gols para todos jogadores.
team = []
dict = {}
list = []

while True:
	dict.clear()
	dict['nome'] = str(input('Nome do jogador: '))
	partidas = int(input('Quantas partidas jogou?: '))
	list.clear()
	for i in range(partidas):
		gols = int(input(f'Quantos gols na partida {i+1}?'))
		list.append(gols)
	dict['gols'] = list
	dict['total'] = sum(list)
	team.append(dict.copy())
	r = str(input('Deseja continuar?')).upper()[0]
	if r in 'N':
		break
print('-'*30)
for i, j in enumerate(team):
	print(f'{i:>3}', end='')
	for d in j.values():
		print(f'{str(d):<15}', end='')
	print()
print(dict)
print('-'*30)
for i, j in dict.items():
	print(f'O campo {i} tem o valor {j}')

print('-' * 30)
print(f'O jogador {dict["nome"]} jogou {len(dict["gols"])} partidas.')
for i, j in enumerate(dict['gols']):
	print(f'-> Na partida {i+1} fez {j} gols.')
print(f'Somando um total de {dict["gols"]} gols.')