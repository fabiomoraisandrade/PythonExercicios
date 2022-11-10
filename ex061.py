'''a1 = int(input('Primeiro termo da P.A: '))
r = int(input('Razão da P.A: '))
c = 1
while c <= 10:
    ac = a1 + (c - 1) * r
    print('{}'.format(ac), end=', ')
    c = c + 1
print('FIM')'''

#2 Modo
a1 = int(input('Primeiro termo da P.A: '))
r = int(input('Razão da P.A: '))
termo = a1
c = 1
while c <= 10:
    print('{}, '.format(termo), end='')
    termo = termo + r
    c = c + 1
print('FIM')






