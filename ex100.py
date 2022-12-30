from random import randint
from time import sleep
def sortlista(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Sorteando os 5 valores da lista: ', end='')
    for c in lista:
        print(f'{c} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for c, v in enumerate(lista):
        if v % 2 == 0:
            soma = soma + v
    print(f'Somando os valores de {lista}, temos {soma}')


#PROGRAMA PRINCIPAL
numero = []
sortlista(numero)
somapar(numero)