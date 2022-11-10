print('='*20)
print('SEQUÊNCIA FIBONACCI')
print('='*20)
n = int(input('Número de termos a serem exibidos: '))
a1 = 0
a2 = 1
print('{}, {}, '.format(a1, a2), end='')
t = 3
while t <= n:
    a3 = a1 + a2
    print('{}, '.format(a3), end='')
    a1 = a2
    a2 = a3
    t = t + 1
print('FIM')
