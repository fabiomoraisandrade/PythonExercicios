'''n = 0
t = 0
s = 0
while n != 999:
    n = int(input('Informe um número inteiro: '))
    t = t + 1
    s = s + n
print('O total de números lidos foi {}'.format(t - 1))
print('A soma dos números informados é {}'.format(s - 999))'''

#Outra maneira de fazer é colocar o comando de informar o número duas vezes. A primeira fora do laço e a segunda dentro
#Dessa forma, a variável soma não estará com o valor errado
t = s = 0
n = int(input('Informe um número inteiro (Digite 999 para parar): '))
while n != 999:
    s = s + n
    t = t + 1
    n = int(input('Informe um número inteiro: '))
print('O total de números inseridos é {}. A soma deles é {}'.format(t, s))
