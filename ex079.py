lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar...')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
lista.sort()
print(f'Os número informados são {lista}')
print('FIM')

#Outra maneira de colocar os números ordenados é {sorted(lista)}