n = int(input('Digite um número inteiro de 1 a 9: '))
print('A tabuada de {} é:'.format(n))
print('-'*12)
for c in range(1, 11):
    m = n * c
    print('{} x {:2} = {}'.format(n, c, m))
print('-'*12)

