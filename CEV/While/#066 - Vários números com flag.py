cont = som = 0
while True:
    num = int(input('Digite um numero inteiro: '))
    if num == 999:
        break
    cont += 1
    som += num
print(f'Foram digitados {cont} numeros e a soma entre eles resulta em {som}')
