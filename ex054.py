from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento {}º: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print('O número de pessoas que atingiram a maioriade é {}'. format(totalmaior))
print('O número de pessaos que atingiram a menoriade é {}'.format(totalmenor))




