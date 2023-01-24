dict = {}
list = []
dict['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas jogou?: '))
for i in range(partidas):
	gols = int(input(f'Quantos gols na partida {i+1}?'))
	list.append(gols)
dict['gols'] = list
dict['total'] = sum(list)
print(dict)
print('-'*30)
for i, j in dict.items():
	print(f'O campo {i} tem o valor {j}')
print('-' * 30)
print(f'O jogador {dict["nome"]} jogou {len(dict["gols"])} partidas.')
for i, j in enumerate(dict['gols']):
	print(f'-> Na partida {i+1} fez {j} gols.')
print(f'Somando um total de {dict["gols"]} gols.')
