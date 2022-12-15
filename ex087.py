'''
soma = 0
maiorl2 = 0
for l in range(0, 3):matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}, {c+1}] [Linha, Coluna]: '))
        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]
        if l == 1 and c == 0:
            maiorl2 = matriz[1][0]
        else:
            if l == 1 and c == 1:
                if matriz[1][1] > maiorl2:
                    maiorl2 = matriz[1][1]
            if l == 1 and c == 2:
                if matriz[1][2] > maiorl2:
                    maiorl2 = matriz[1][2]
somac3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('-'*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-'*40)
print(f'A soma dos valores pares da matriz é {soma}')
print(f'A soma dos valores da 3º coluna da matriz é {somac3}')
print(f'O maior valor da 2º linha é {maiorl2}')'''

# MANEIRA MAIS INTELIGENTE DE SOMAR OS ELEMENTOS DA 3 COLUNA E MOSTRAR O MAIOR NÚMERO DA 2 LINHA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somac3 = maiorl2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l+1}, {c+1}] [Linha, Coluna]: '))
        if matriz[l][c] % 2 == 0:
            somapar = somapar + matriz[l][c]
print('-'*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-'*40)
print(f'A soma dos números pares da matriz é {somapar}')
for l in range(0, 3):
    somac3 = somac3 + matriz[l][2]
print(f'A soma dos números da 3º coluna é {somac3}')
for c in range(0, 3):
    if c == 0:
        maiorl2 = matriz[1][c]
    elif matriz[1][c] > maiorl2:
        maiorl2 = matriz[1][c]
print(f'O maior número da 2º linha é {maiorl2}')
