print('='*30)
print('{:^30}'.format('BANCO FMA'))
print('='*30)
valor = int(input('Valor a sacar: R$'))
total = valor
ced = 50
totalcedula = 0
while True:
    if total >= ced:
        total = total - ced
        totalcedula = totalcedula + 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalcedula = 0
        if total == 0:
            break
print('-'*30)
print('O banco FMA agradece sua preferência. Volte sempre!')