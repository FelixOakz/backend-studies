tot = cont = num = 0
while num != 999:
    tot += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Foram digitados {cont-1} e a soma entre eles foi {tot}')