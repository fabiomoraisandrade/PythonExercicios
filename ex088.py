from random import randrange
from time import sleep
print('-'*50)
print(f'{"GERADOR DE JOGOS MEGA SENA":^50}')
print('-'*50)
lista = []
jogos = []
n = int(input('Número de jogos a sortear: '))
total = 1
while total <= n:
    cont = 0
    while True:
        num = randrange(1, 61)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    total = total + 1
    lista.clear()
print('-'*10, f'Sorteando {n} jogos', '-'*10)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('Boa Sorte!')