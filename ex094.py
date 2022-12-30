geral = dict()
lista = []
total = 0
while True:
    geral['nome'] = str(input('Nome: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    geral['sexo'] = sex
    geral['idade'] = int(input('Idade: '))
    total = total + geral['idade']
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    lista.append(geral.copy())
    if continuar == 'N':
        break
media = total/(len(lista))
print('-'*40)
print(f'A) O número de pessoas cadastradas é {len(lista)}')
print(f'B) A média de idade é de {media:.2f} anos')
print('C) As mulheres cadastradas foram', end=' ')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média')
'''for p in lista:
    if p['idade'] > media:
        print(f'{p}')'''
#Solução do Guanabara para a letra D
for p in lista:
    if p['idade'] > media: #p é um dicionário
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO')
#Pelo que eu entendi, nos dicionários não acumuam os valores como as listas. Em um laço infinito, a cada ve que você
#adiciona um novo valor no dicionário, ele é substituido. Então não faz muito sentido apagar os dados do dicionário
#a cada vez que vai realizar um loop para entrada de dados, pois eles serão substituídos
