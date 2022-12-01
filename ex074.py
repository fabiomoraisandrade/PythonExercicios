from random import randrange
n = (randrange(0, 100), randrange(0, 100), randrange(0, 100), randrange(0, 100), randrange(0, 100))
print('Os valores sorteados foram: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado é {max(n)}')
print(f'O menor valor sorteado é {min(n)}')
