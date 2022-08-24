termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razao da PA: '))
tamPA = 10
ultimotermo = termo + (razao*tamPA)

while termo != ultimotermo:
    print(f'{termo}', end=' | ')
    termo += razao

    if termo == ultimotermo:
        tamPA = int(input('\nQuantos termos quer a mais?: '))
        ultimotermo = termo + (razao * tamPA)

        while termo != ultimotermo:
            print(f'{termo}', end=' | ')
            termo += razao

print('\nPrograma encerrado.')

