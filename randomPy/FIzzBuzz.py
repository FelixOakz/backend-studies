# for loop para printar numeros de zero a cem
for i in range(1, 101):
    # condicoes diferenciadas de acordo com resultado esperado
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    print(i)