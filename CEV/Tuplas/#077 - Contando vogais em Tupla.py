"""
tupla com varias palavras, depois deve mostrar para cada palavra, quais sao suas vogais

"""
from prompt_toolkit import output

palavras = (
	'aprender',
	'curso',
	'trabalhar',
	'programar',
	'gratis',
	'estudar',
	'mercado',
	'python',
	'linguagem',
	'praticar',
	'programador',
	'futuro'
)
for letras in palavras:
	print(f'\nNa palavra {letras} temos: ', end='')
	for letra in letras:
		if letra in 'aeiou':
			print(f'{letra.upper()}', end=' ')
