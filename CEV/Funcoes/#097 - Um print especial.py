def printar(text):
	tam = len(text) + 4
	print(f'{"-"*tam}\n  {text}\n{"-"*tam}')

while True:
	text = str(input('Escreva texto: '))
	if text == 'exit':
		break
	printar(text)
