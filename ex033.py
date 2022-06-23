'''n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outroo número: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    print('O número {} é o maior dentre os 3 e o número {} é o menor'.format(n1, n3))
if n2 > n1 and n2 > n3 and n1 > n3:
    print('O número {} é o maior dentre os 3 e o número {} é o menor'.format(n2, n3))
if n3 > n1 and n3 > n2 and n2 > n1:
    print('O número {} é o maior dentre os 3 e o número {} é o menor'.format(n3, n1))
if n1 > n2 and n1 > n3 and n3 > n2:
    print('O número {} é o maior dentre os 3 e o número {} é o menor'.format(n1, n2))
if n2 > n1 and n2 > n3 and n3 > n1:
    print('O número {} é o maior dentre os 3 e o número {} é o menor'.format(n2, n1))
if n3 > n1 and n3 > n2 and n1 > n2:
    print('O número {} é o maior dentre os 3 e o número {} é o menor'.format(n3, n2))'''

a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

