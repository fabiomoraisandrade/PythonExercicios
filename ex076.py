n = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20', 'Compasso', '9.99',
     'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
for c in range(0, len(n)): #c é a posição e n[c] é a variável que está na posição c
    if c %2 == 0:
        print(f'{n[c]:.<40}', end='')
    else:
        print(f'R${n[c]:>6}')
print('-'*50)
#poderia crar a tupla com os preços sem estar entre '', como números e não como strings.
#Poderia usar a formatação print(f'R${n[c]:>6.2f}' para formatar os números com 2 casas decimais.