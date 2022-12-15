'''lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja contonuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*50)
print(f'A lista completa é {lista}')
print(f'A lista dos números pares é {listap}')
print(f'A lista dos números ímpares é {listai}')'''

#2 MANEIRA
lista = []
listap = []
listai = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for v, c in enumerate(lista):
    if c % 2 == 0:
        listap.append(c)
    else:
        listai.append(c)
print('-'*50)
print(f'A lista completa é {lista}')
print(f'A lista dos números pares é {listap}')
print(f'A lista dos números ímpares é {listai}')
