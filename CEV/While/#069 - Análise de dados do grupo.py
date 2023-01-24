maiores = homens = mulhermenor = 0
while True:
    id = int(input('Idade?: '))
    sex = str(input('Sexo? [M/F]: ')).strip().upper()[0]
    if id >= 18:
        maiores += 1
    if sex == 'M':
        homens += 1
    if sex == 'F' and id <= 20:
        mulhermenor += 1
    opt = str(input('>>> Deseja continuar?[S/N]: ')).strip().upper()[0]
    if opt == 'N':
        break
print(f'\nDas pessoas entrevistadas: Temos {maiores} maiores de idade,'
      f' {homens} Homens cadastrados,'
      f' e {mulhermenor} mulheres com menos de 20 anos.')
