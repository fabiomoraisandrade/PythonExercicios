def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a} m²')


#PROGRAMA PRINCIPAL
print(f'{"Controle de Terrenos":^30}')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)