sexo = str(input('Qual seu sexo? (M/F): ')).strip().upper()[0] #o comando [0] é um fatiamento para pegar apenas a primeira letra informada. Se o usuario digitar Masculino, a letra registrada será M
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe seu sexo (M/F): ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
