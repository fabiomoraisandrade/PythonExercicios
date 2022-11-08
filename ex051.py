n = int(input('Informe o primeiro termo da progressão aritmética: '))
r = int(input('Informe a razão da PA: '))
decimo = n + (10 - 1) * r
for c in range(n, decimo + r, r):
    print('{}'.format(c), end=' -> ')
print('Acabou')
