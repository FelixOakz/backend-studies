def Leiaint(msg):
	while True:
		try:
			n = int(input(msg))

		except (ValueError, TypeError):
			print('Provavelmente vc digitou errado.')
			continue

		except KeyboardInterrupt:
			print('Usuario preferiu nao informar dados.')
			return 0
		else:
			return n


num = Leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')
