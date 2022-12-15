#MINHA SOLUÇÃO (LONGE DE SER A MELHOR)
'''principal = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media = (dados[1] + dados[2])/2
    dados.append(media)
    principal.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*50)
print(f'{"Nº": <10} {"Nome":^10} {"Média":>15}')
print('-'*50)
for pos, v in enumerate(principal):
    print(f'{pos: <10}', end='')
    print(f'{v[0]:^11}', end='')
    print(f'{v[3]:>15.2f}')
print('-'*50)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    for pos, v in enumerate(principal):
        if notas == pos:
            print(f'Notas de {v[0]} são {v[1]} e {v[2]}')
    if notas == 999:
        break'''
#SOLUÇÃO MELHOR
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*30)
print(f'{"Nº":<4} {"Nome":<10} {"Média":>8}')
print('-'*30)
for pos, v in enumerate(ficha):
    print(f'{pos:<4} {v[0]:<10} {v[2]:>8.2f}')
print('-'*30)
#Jeito do professor Guanabara
while True:
    print('-'*40)#Enfeitar
    notas = int(input('Mostrar notas de qual aluno? (999 para encerrar): '))
    if notas <= len(ficha) - 1: #Ficha tem compimento do número de alunos inseridos. Se o número de alunos for 2, as posições deles serão 0 e 1. Se eu quiser o aluno 0, 0 é menor que 2-1. Então mostrará a lista na posição 0 que contem as sublistas de nome, notas e média. Para exibir as notas, elas estão na posição 1, por isso ficha[notas][1]
        print(f'As notas de {ficha[notas][0]} são {ficha[notas][1]}')
    if notas == 999:
        break
#while True:   #PARA MIM, ASSIM É MELHOR
#    notas = int(input('Mostrar notas de qual aluno? (999 para encerrar): '))
#    for pos, v in enumerate(ficha):
#        if notas == pos:
#            print(f'Notas de {v[0]} são {v[1]}')
#    if notas == 999:
#        break
