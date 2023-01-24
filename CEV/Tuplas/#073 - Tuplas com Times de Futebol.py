"""
tupla com os 20 primeiros colocados camp. brasileiro
a: apenas os 5 primeiros colocados
b: os ultimos 4 colocados
c: uma lista com os times em ordem alfabetica
d: em que posical da tabela esta o time chapecoense
"""
times =(
	'PALMEIRAS',
	'INTERNACIONAL',
	'FLAMENGO',
	'FLUMINENSE',
	'CORINTHIANS',
	'ATHLETICO-PR',
	'ATLETICO-MG',
	'AMERICA-MG',
	'GOIAS',
	'SANTOS',
	'RED BULL BRAGANTINO',
	'BOTAFOGO',
	'SAO PAULO',
	'CEARA',
	'FORTALEZA',
	'CORITIBA',
	'CUIABA',
	'AVAI',
	'ATHLETICO-GO',
	'JUVENTUDE'
)
print(f'Primeiros 5 colocados: {times[0:5]}')
print(f'Ultimos 4 colocados: {times[-4:]}')
print(f'Lista com ordem alfababetica: {sorted(times)}')
print(f'Flamengo se encontra na {times.index("FLAMENGO")+1}ª posicao na lista')