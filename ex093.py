dados = dict()
golpartidas = list()
tot = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for p in range(0, partidas):
    golpartidas.append(int(input(f'Quantos gols na partida {p}? ')))
    tot = tot + golpartidas[p]
dados['gols'] = golpartidas[:] #Importante criar a cópia para não ter ligação com a lista
#dados['total'] = sum(golpartidas)  Já soma os gols sem precisar criar uma variável tot
dados['total'] = tot
print('-'*40)
print(dados)
print('-'*40)
for k, v in dados.items():
    print(f'  - O campo {k} tem o valor {v}.')
print('-'*40)
print(f'O Jogador {dados["nome"]} jogou {partidas}.')
for i, j in enumerate(golpartidas):                    #Essa última parte também dá pra fazer como comentado abaixo
    print(f'  =>Na partida {i}, fez {j} gols.')
print(f'Foi um total de {tot} gols')
'''for i, v in enumerate(dados['gols']):
    print(f'  =>O jogador {dados["nome"]} fez {v} gols')  #Os gols estão guardados em uma lista dentro do dicionário
print(f'Foi um total de {dados["total"]} gols')'''