t = int(input('Primeiro termo da PA: '))
r = int(input('Razao da PA: '))
tamPA = 10
ultimoT = t + (r * tamPA)

while t != ultimoT:
    print(f'{t}', end=' | ')
    t += r

    while tamPA != 0:
        if t == ultimoT:
            tamPA = int(input('\nQuantos termos quer a mais?: '))
            ultimoT = t + (r * tamPA)

            while t != ultimoT:
                print(f'{t}', end=' | ')
                t += r
print('\nPrograma encerrado.')


#ao finalizar testado e funcionando. algo quebrou e corrija depois!