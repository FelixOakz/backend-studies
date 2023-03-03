from random import randint
from time import sleep
from operator import itemgetter
dict = dict()
for c in range (1, 5):
    dict[f'jogador {c}'] = randint(1, 6)
ranking = list()
print('Valores sorteados:')
for k, v in dict.items():
    print(f'{k} tirou {v} no dado.')
    sleep (.5)
ranking = sorted(dict.items(), key=itemgetter(1), reverse=True)
print('------- Classificacao -------')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep (.5)
