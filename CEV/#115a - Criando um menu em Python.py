def writing(nome='desconhecido', idade=0):
    try:
        import os
        filepath = os.path.abspath('CEV/cevdatabase.txt')
        file = open(filepath, 'at')
        file.write(f'{nome},{idade}\n')
        file.close()
    except IOError:
        print('\033[0;31mFile not found or path is incorrect!\033[m\n')


def reading():
    try:
        import os
        filepath = os.path.abspath('CEV/cevdatabase.txt')
        file = open(filepath, 'r+')
        for linha in file:
            data = linha.split(',')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<34}{data[1]:>3} anos')
    except IOError:
        print('\033[0;31m - Nao ha pessoas cadastradas!\033[m')
        


def line(tam = 42):
    return '-'* tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def separador(simb):
    print(f'{simb}'*30)


def menu():
    header('Menu Principal')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do programa')
    print(line())


if __name__ == '__main__':
    while True:
        menu()
        option = input('Escolha opcao: ')
        if option == '1':
            header('Pessoas cadastradas:')
            reading()

        elif option == '2':
            header('Cadastrar pessoa:')
            nome = str(input('Digite o nome: ')).strip().capitalize()
            idade = int(input('Digite a idade: '))
            writing(nome, idade)
            print('\033[0;32m\n   Registro adicionado com sucesso!\033[m')

        elif option == '3':
            header('Saindo do sistema')
            break
        else:
            print('\033[0;31mEscolha uma opcao adequada!\033[m')
