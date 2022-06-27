s = 0
i = 0
for c in range (1, 7):
    n = int(input('Número inteiro {}º: '.format(c)))
    if n % 2 == 0:
        s = s + n
        i = i + 1
print('Você informou {} números PARES. A soma dos números pares informados é {}'.format(i, s))
