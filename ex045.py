from random import randrange
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randrange(0, 3)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogador > 2:
    print('Jogada Inválida. Tente novamente')
else:
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
if computador == 0:
    if jogador == 0:
            print('Empate')
    elif jogador == 1:
            print('Jogador Venceu')
    else:
            print('Computador Venceu')
elif computador == 1:
    if jogador == 0:
            print('Computador Venceu')
    elif jogador == 1:
            print('Empate')
    else:
            print('Jogador Venceu')
elif computador == 2:
    if jogador == 0:
            print('Jogador Venceu')
    elif jogador == 1:
            print('Computador Venceu')
    elif jogador == 2:
            print('Empate')









