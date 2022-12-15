'''galera = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*50)
print(f'Foram cadastradas {len(galera)} no total')
print(f'O maior peso cadastrado é de {maior} kg. Peso correspondente a ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso cadastrado é de {menor} kg. Peso correspondente a ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')'''

#OUTRO JEITO
galera = []
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    if len(galera) == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    galera.append([nome, peso])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(galera)
print(f'O número de pessoas cadastradas é {len(galera)}')
print(f'O maior peso é {maior} kg. Peso correspondente a ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso é {menor} kg. Peso correspondente a ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
