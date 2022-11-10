r = 'S'
t = 0
s = 0
maior = 0
menor = 0
while r == 'S':
    n = int(input('Informe um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Dados inválidos. Deseja Continuar? [S/N] ')).strip().upper()[0]
    s = s + n
    t = t + 1
    if t == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
m = s / t
print('A média dos valores informados é {:.2f}'.format(m))
print('O maior número informado é {} e o menor é {}'.format(maior, menor))

