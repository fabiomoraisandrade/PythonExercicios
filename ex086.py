matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}, {c+1}] [Linha, Coluna]: ')) #Irá colocar os valores na linha l e na coluna c.
print('-'*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='') #Mostra a matriz na linha zero e nas colunas 0, 1, 2. Depois na linha 1 nas colunas 0, 1, 2.
    print() #Quebra uma linha quando acaba de completar uma linha da matriz. Assim a matriz irá aparecer formatada direitinho
