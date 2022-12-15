lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
lista.sort(reverse=True)
print('-'*50)
print(f'O número de valores digitados foram {len(lista)}')
print(f'Os números inseridos em ordem decrescente é {lista}')
if 5 in lista:
    for c in range(0, len(lista)):
        if lista[c] == 5:
            print(f'O número 5 está na posição {c} da lista')
else:
    print('O número 5 não está na lista')
