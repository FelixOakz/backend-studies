from random import randint
vitorias = 0
while True:
    player = int(input('Digite um valor [0 a 10]: '))
    pc = randint(1, 10)
    decisao = input('Par ou Impar? [P/I]: ').strip().upper()
    while decisao not in 'PI':
        decisao = input('Par ou Impar? [P/I]: ').strip().upper()
    if (player + pc) % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print(f'Voce jogou {player} e o computador jogou {pc}, total de {player + pc} sendo {result}')
    if decisao == result.strip()[0]:
        print('Voce VENCEU! \nVamos outra rodada....')
        vitorias += 1
    else:
        print('Game Over...')
        break
print(f'Voce Perdeu! Mas parabens pelas {vitorias} vitorias.')
