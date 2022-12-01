lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Inserindo ao final da lista')
    else:
        for pos in range(0, len(lista)):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Inserindo na posição {pos} da lista')
print(f'Os valores digitados em ordem são {lista}')

