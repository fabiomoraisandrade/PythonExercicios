'''valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Valor para a posição {c}: ')))
print('-'*30)
print(f'Você Digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'{pos}.. ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == min(valores):
        print(f'{pos}.. ', end='')'''
#Pode-se reutilizar os nomes pos e v para os laços for

#2 MANEIRA
valores = []
maior = menor = 0
for c in range(0, 5):#c é a posição e valores[c] é a variável que está na posição c
    valores.append(int(input(f'Valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores [c]
print('-'*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor é {maior} nas psoições ', end='')
for i, v in enumerate(valores):#v é a variável de valores e i é a posição
    if v == maior:
        print(f'{i}.. ', end='')
print(f'\nO menor valor é {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}.. ', end='')

