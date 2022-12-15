'''principal = []
pares = []
impares = []
for c in range(1, 8):
    n = int(input(f'{c}º Número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
principal.append(pares[:])
principal.append(impares[:])
pares.clear()
impares.clear()
print(principal)
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores ímpares digitados foram: {principal[1]}')'''

#MANEIRA CORRETA SEGUNDO O ENUNCIADO QUE PEDE PARA FAZER SOMENTE 1 LISTA
principal = [[], []]
for c in range(1, 8):
    valor = int(input(f'{c}º número: '))
    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)
principal[0].sort()
principal[1].sort()
print('-'*40)
print(f'Os números pares digitados foram: {principal[0]}')
print(f'Os números ímpares digitados foram: {principal[1]}')

