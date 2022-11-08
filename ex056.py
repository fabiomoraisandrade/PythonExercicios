sidade = 0 #soma das idades
maioridadeh = 0 #homem mais velho
nomevelho = '' #nome do homem mais velho
im = 0 #contador (número de mulheres menores de 20 anos)
for c in range(1, 5):
    print('---------- {}ª PESSOA ----------'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    sidade = sidade + idade
    midade = sidade/4
    if c == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
            maioridadeh = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        im = im +1
print('A média das idades informadas é {} anos'.format(midade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadeh, nomevelho))
print('O número de mulheres que tem menos de 20 anos é {}'.format(im))



