from random import randrange
n = randrange(0, 5)
print('O computador escolherá um número inteiro entre 0 e 5. Você deverá inserir um número para descobrir se acertou ou não.')
m = int(input('Digite um número inteiro de 0 a 5: '))
if m == n:
    print('Parabéns, você acertou')
else:
    print('Que pena, você errou. O número escolhido foi {}'.format(n))



