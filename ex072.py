'''n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
v = int(input('Informe um número de 0 a 20: '))
while v < 0:
    v = int(input('Dados inválidos. Informe um número de 0 a 20: '))
while v > 20:
    v = int(input('Dados inválidos. Informe um número de 0 a 20: '))
print(f'Você digitou o número {n[v]}')'''

#Segunda maneira

'''n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    v = int(input('Informe um número de 0 a 20: '))
    if 0 < v < 20:
        break
    else:
        print('Dados inválidos. ', end='')
print(f'Você digitou o número {n[v]}')'''

#Fazendo o programa perguntar se deseja continuar
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    v = int(input('Informe um número de 0 a 20: '))
    if 0 < v < 20:
        print(f'Você digitou o número {n[v]}')
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
    else:
        print('Dados inválidos', end='')
print('Fim do programa')