def fatorial(num, show=False):
	"""
	-> Calcula o fatorial de um numero arbitrario
	:param num: o numero a ser calculado
	:param show: opcional, caso queira o calculo por extenso
	:return: o valor fatorial de um numero.
	"""
	c = num
	f = 1
	while c > 0:
		if show == True:
			print(f'{c}', end='')
			print(' x ' if c > 1 else ' = ', end='')
		f *= c
		c -= 1
	print(f)

help(fatorial)

