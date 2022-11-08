n = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total = total + 1
        print('\033[34m', end='') #código para destacar em azul os números que forem divisíveis por n
    else:
        print('\033[m', end='') #código para deixar normal (desaplicar a cor) dos números que não forem divisíveis por n
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('Portanto o número {} É PRIMO'.format(n))
else:
    print('Portanto o número {} NÃO É PRIMO'.format(n))

