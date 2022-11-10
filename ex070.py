nome = str('LOJAS SUPER BARATÃO')
print('-'*30)
print('{:^30}'.format(nome))
print('-'*30)
soma = 0
pmil = 0
c = 1
maior = 0
menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    if c == 1:
        maior = preço
        menor = preço
        barato = produto
        c = c + 1
    else:
        if preço > maior:#Essa parte não precisa pois não quer saber qual foi o produto mais caro
            maior = preço
        elif preço < menor:#Esse bloco pode ser simplificado colocando no primeiro if como or preço < menor
            menor = preço
            barato = produto
    if preço >= 1000:
        pmil = pmil + 1
    soma = soma + preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar ==  'N':
        break
print('-------------------- FIM --------------------')
print(f'O total dacompra foi R${soma:.2f}')
print(f'O número de produtos que custam mais de R$1000,00 é {pmil}')
print(f'O produto mais barato é {barato} que custa R${menor:.2f}')
