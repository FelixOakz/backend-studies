def readvalue(msg):
	valido = False
	while not valido:
		ent = str(input(msg)).replace(',', '.')
		if ent.isalpha() or ent.strip() == '':
			print(f'\033[0;31mERROR {ent}: Invalid command.\033[m')
		else:
			valido = True
			return float(ent)


def leiaInt(msg):
	ok = False
	valor = 0
	while True:
		n = str(input(msg))
		if n.isnumeric():
			valor = int(n)
			ok = True
		else:
			print('\033[0;31m Erro, digite um valor valido.\033[m')
		if ok:
			break
	return valor