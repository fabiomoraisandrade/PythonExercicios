from random import randrange
from time import sleep
from operator import itemgetter
jogadado = {'Jogador 1': randrange(1, 7), 'Jogador 2': randrange(1, 7),
            'Jogador 3': randrange(1, 7), 'Jogador 4': randrange(1, 7)}
ranking = {} #Pode ser uma lista já que a função itemgetter que colocar os resultados de um dicionário em ordem vira uma lista de tuplas
for k, v in jogadado.items():
    print(f'{k} tirou {v}')
    sleep(1)
ranking = sorted(jogadado.items(), key=itemgetter(1), reverse=True) #O  comando key=itemgetter(1) coloca os resultados do dado (posição 1) em ordem crescente. Por isso tem o reverse=True
print('-'*30)
print('  ----- RANKING DOS JOGADORES -----')
#print(ranking) Só para ver que o ranking sai com uma lista de tuplas. Portanto para exibir com o laço for, tem que ser tratado como lista e tupla
for i, v in enumerate(ranking):
    print(f'  - {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
