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
