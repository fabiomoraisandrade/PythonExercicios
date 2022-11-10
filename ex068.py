'''from random import randrange
print('='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('='*30)
t = 0
while True:
    comp = randrange(0, 11)
    n = int(input('Informe um valor: '))
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    soma = comp + n
    if soma % 2 == 0 and opção == 'P':
        print(f'Você jogou {n} e o computador jogou {comp}. O total é {soma}: Número PAR')
        print('Você VENCEU!!')
        print('Vamos jogar novamente...')
        print('-'*30)
        t = t + 1
    elif soma % 2 == 0 and opção == 'I':
        print(f'Você jogou {n} e o computador jogou {comp}. O total é {soma}: Número PAR')
        print('Você PERDEU')
        print('-'*30)
        break
    elif soma % 2 == 1 and opção == 'P':
        print(f'Você jogou {n} e o computador jogou {comp}. O total é {soma}: Número ÍMPAR')
        print('Você PERDEU')
        print('-'*30)
        break
    elif soma % 2 == 1 and opção == 'I':
        print(f'Você jogou {n} e o computador jogou {comp}. O total é {soma}: Número ÍMPAR')
        print('Você VENCEU!!')
        print('Vamos jogar novamente...')
        t = t + 1
print('GAME OVER')
print(f'Voce Venceu {t} vezes.')'''


from random import randrange
print('-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-'*30)
t = 0
while True:
    comp = randrange(0, 11)
    n = int(input('Informe um valor: '))
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    soma = comp + n
    print(f'Você jogou {n} e o computador jogou {comp}. O total é {soma}: ', end='')
    if opção == 'P':
        if soma %2 == 0:
            print('Número PAR')
            print('-'*30)
            print('Você GANHOU!!!')
            t = t + 1
        else:
            print('Número ÍMPAR')
            break
    elif opção == 'I':
        if soma %2 == 0:
            print('Número PAR')
            break
        else:
            print('Número ÍMPAR')
            print('-'*30)
            print('Você GANHOU!!!')
            t = t + 1
    print('Vamos jogar novamente...')
print('-'*30)
print('GAME OVER!')
print(f'Você venceu {t} vezes.')



