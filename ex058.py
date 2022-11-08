from random import randrange
'''n = randrange(0, 11)
c = 1
j = int(input('Pensei em um número de 0 a 10. Qual número eu pensei? '))
while j != n:
    j = int(input('Errou vacilão. Tente novamente: '))
    c = c+1
print('Parabéns você acertou! Seu número de palpites foram {}'.format(c))'''
n = randrange(0, 11)
print('Pensei em um número entre 0 e 10. Você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    j = int(input('Qual seu palpite? '))
    palpite = palpite + 1
    if j == n:
        acertou = True
    else:
        if j < n:
            print('Um pouco mais... Tente novamente.')
        else:
            print('Um pouco menos... Tente novamente.')
print('Acertou com {} tentativas. Parabéns'.format(palpite))

