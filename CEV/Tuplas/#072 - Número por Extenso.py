extenso = "zero", "um", "dois", "três","quatro","cinco","seis","sete",\
		  "oito","nove","dez","onze","doze","treze","catorze",\
		  "quinze","dezesseis","dezessete","dezoito","dezenove","vinte",
while True:
	num = int(input('Digite um numero entre 0 e 20: '))
	if 0 <= num <= 20:
		break
	print('Por favor, entre ZERO e VINTE!')
print(f'Este valor por extenso eh {extenso[num]}')