def ajuda(comando):
	help(comando)


def title():
	print('-'*25)
	print('PYTHON INTERACTIVE HELP')
	print('-'*25)


comando = ''
while True:
	title()
	comando = str(input('Library or function: '))
	if comando.upper() == 'FIM':
		break
	else:
		ajuda(comando)
