from random import randint
from time import sleep
jogos = []
lista = []
print('-'*30, '>       JOGOS NA MEGA','-'*30, sep='\n')
jogo = int(input('Quantos jogos voce quer?: '))
print(f'\n> Sorteando {jogo} jogos:')
for i in range(jogo):
	for i in range(6):
		lista.append(randint(0, 60))
	jogos.append(lista[:])
	lista.clear()
for i in range(jogo):
	print(f'Jogo {i+1}:', *jogos[i])
	sleep(.7)
