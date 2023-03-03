somaidade = mulhersub20 = idhomemvelho = 0
nomevelho = ' '
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if sexo in 'Mm' and idade > idhomemvelho:
        idhomemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhersub20 += 1
print(f'\nA media de idade do grupo eh de {somaidade/4}anos.')
print(f'O homem mais velho tem {idhomemvelho} anos e se chama {nomevelho}.')
print(f'Ao todo sao {mulhersub20} mulheres com menos de 20 anos.')
