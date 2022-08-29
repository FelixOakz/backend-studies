opcao = 'S'
cont = soma = maior = menor = 0
while opcao != 'N':
    num = int(input('Digite um numero:  '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('-     Deseja continuar?  ')).strip().upper()
print(f'Voce digitou {cont} numeros e a media foi {soma / cont:.2f}.')
print(f'o maior valor foi {maior} e o menor valor foi {menor}.')

#melhorar com conceitos aprendidos na prox passada
