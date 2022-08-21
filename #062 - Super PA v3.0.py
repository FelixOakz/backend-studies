termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razao da PA: '))
fim = 10
decimo = termo + (razao*fim)

while termo != 0:
    if termo != decimo:
        print(f'{termo}', end=' - ')
        termo += razao

    if termo == decimo:
        ntermos = int(input('\nQuantos termos voce quer mostrar a mais?: '))
        fim = ntermos
        while termo != fim:
            novofim = termo + (razao*fim)
            termo += razao
            print(f'{termo}', end=' - ')

# printar mais 1 termo da pa com razao R


print('\nPrograma encerrado.')
