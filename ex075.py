n = (int(input('Primeiro número inteiro: ')), int(input('Segundo número inteiro: ')),
     int(input('Terceiro número inteiro: ')), int(input('Quarto número inteiro: ')))
print(f'O número 9 apareceu {n.count("9")} vezes')
if 3 in n:
    print(f'O número 3 foi digitado na {n.index(3) + 1}ª posição')
else:
    print(f'O número 3 não foi digitado')
print('Os números pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c} ', end='')
