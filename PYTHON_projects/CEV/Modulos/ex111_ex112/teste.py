from utilidades import moeda
from utilidades import dados

p = dados.readvalue('Enter the value in R$: ')
moeda.resumo(p, 35, 22)
