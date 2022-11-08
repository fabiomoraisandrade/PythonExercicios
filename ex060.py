'''from math import factorial                        1 JEITO
n = int(input('Informe um número inteiro: '))
fac = factorial(n)
print('O fatorial de {} é {}'.format(n, fac))'''

'''n = int(input('Digite um número: '))              2 JEITO
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = f * c #Calcula o fatorial de fato. A cada repetição ele vai fazendo 1*5*4*3*2*1
    c = c - 1
print('{}'.format(f))'''

n = int(input('Digite um número: '))               # 3 JEITO
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range (n, 0, -1):
    if c > 0:
        print('{}'.format(c), end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        f = f * c
print('{}'.format(f))




