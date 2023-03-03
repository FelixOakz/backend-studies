def aumentar(p, val, formato=False):
	res = p + (p * val / 100)
	return res if formato is False else moeda(res)


def diminuir(p, val, formato=False):
	res = p - (p * val / 100)
	return res if formato is False else moeda(res)


def dobro(p, formato=False):
	res = p * 2
	return res if not formato else moeda(res)


def metade(p, formato=False):
	res = p / 2
	return res if not formato else moeda(res)


def moeda(val):
	return f'R${val:.2f}'


def resumo(p=0, plus=0, less=0):
	print('-'*30)
	print('RESUMO DO VALOR'.center(30))
	print('-' * 30)
	print(f'Preco analisado: \t\t{moeda(p)}')
	print(f'O dobro equivale: \t\t{dobro(p, True)}')
	print(f'A metade equivale: \t\t{metade(p, True)}')
	print(f'Aumentando em {plus}%:  \t{aumentar(p, 10)}')
	print(f'Diminuindo em {less}%: \t\t{diminuir(p, 13)}')
