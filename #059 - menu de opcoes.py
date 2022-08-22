n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
user = 0
while user !=5:
    user = int(input('[1] somar \n[2] multiplicar \n[3] maior numero \n[4] novos numeros \n[5] sair do programa \n>>> Qual eh a sua opcao?: '))
    if user == 1:
        print(f'↓\nA soma de {n1} e {n2} resulta em {n1 + n2}\n ----------')
    elif user == 2:
        print(f'↓\nA multiplicacao de {n1} e {n2} resulta em {n1 * n2}\n ----------')
    elif user == 3:
        print(f'↓\nEntre {n1} e {n2} o maior valor sera {max(n1, n2)}\n ----------')
    elif user == 4:
        print('\nDigite novos numeros: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif user == 5:
        print('')
    else:
        print('\nOpcao invalida! tente novamente.')
print('\nPrograma encerrado.')