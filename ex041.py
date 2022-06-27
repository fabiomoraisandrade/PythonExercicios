from datetime import date
n = int(input('Qual o ano de nascimento do atleta? '))
atual = date.today().year
idade = atual - n
print('Idade do atleta: {} anos'.format(idade))
if idade < 9:
    print('Categoria do atleta: MIRIM.')
elif 14 > idade >= 9:
    print('Categoria do atleta: INFANTIL.')
elif 19 > idade >=  14:
    print('Categoria do atleta: JUNIOR.')
elif 20 > idade >= 19:
    print('Categoria do atleta: SÊNIOR.')
else:
    print('Categoria do atleta: MASTER.')
