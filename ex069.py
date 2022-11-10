nome = str('CADASTRE UMA PESSOA')
ci = 0
ch = 0
cm = 0
while True:
    print('-'*30)
    print('{:^30}'.format(nome))
    print('-'*30)
    idade = int(input('Idade: '))
    if idade > 18:
        ci = ci + 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        ch = ch + 1
    if idade < 20 and sexo == 'F':
        cm = cm + 1
    continuar = ' '
    while continuar not in 'S':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
    if continuar == 'N':
        break
print('=========== FIM DO PROGRAMA ===========')
print(f'O número de pessoas com mais de 18 anos é {ci}')
print(f'O número de homens cadastrado é {ch}')
print(f'O número de mulheres com menos de 20 anos é {cm}')
