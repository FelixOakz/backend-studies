print('='*30)
print(f"{'BDB - Banco dos Brothers':^30}")
print('='*30)
notas50 = notas20 = notas10 = notas1 = totced = 0
while True:
    valor = int(input('Insira o valor que deseja sacar(R$): '))
    while valor >= 50:
        valor -= 50
        notas50 += 1
        totced += 1
    while valor >= 20:
        valor -= 20
        notas20 += 1
        totced += 1
    while valor >= 10:
        valor -= 10
        notas10 += 1
        totced += 1
    while valor >= 1:
        valor -= 1
        notas1 += 1
        totced += 1
    break
print(f'\n> Lhe serao entregues {totced} cedulas no total, sendo:')
if notas50 != 0:
    print(f'{notas50} notas de R$50,',end='')
if notas20 != 0:
    print(f' {notas20} notas de R$20,',end='')
if notas10 != 0:
    print(f' {notas10} notas de R$10,',end='')
if notas1 != 0:
    print(f' {notas1} notas de R$1. Bom dia!')
