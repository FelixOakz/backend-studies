while True:
    val = int(input('Quer ver a tabuada de que valor?: '))
    if val < 0:
        break
    for i in range(1, 11):
        print(f'{val} * {i} = {val*i}')
print('Programa de tabuada encerrado.')
