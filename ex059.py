from time import sleep
v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
opção = 0
while opção != 5:
    print('''-------- MENU DE OPÇÕES --------
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR NÚMERO
    [ 4 ] INSERIR NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Selecione uma opção: '))
    if opção == 1:
        print('A soma de {} e {} é {}'.format(v1, v2, v1 + v2))
    elif opção == 2:
        print('O produto de {} e {} é {}'.format(v1, v2, v1 * v2))
    elif opção == 3:
        if v1 < v2:
            print('O maior valor entre {} e {} é {}'.format(v1, v2, v2))
        else:
            print('O maior valor entre {} e {} é {}'.format(v1, v2, v1))
    elif opção == 4:
        v1 = int(input('Valor 1: '))
        v2 = int(input('Valor 2: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    sleep(1.5)
print('Fim do programa!')
