while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(f'A tabuada de {n} é :')
    print('-'*15)
    for c in range (1, 11):
        print(f'{n} x {c:2} = {n*c:2}')
    print('-'*15)
print('PROGRAMA TABUADA ENCERRADO')
