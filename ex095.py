dados = dict()
golspartidas = list()
lista = list()
while True:
    dados.clear()#Não sei porque é necessário. Explicação no final do código
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas o {dados["nome"]} jogou? '))
    golspartidas.clear() #Precisa limpar porque se não os gols do jogador anterior serão adicionados nos gols dos proximos jogaroes
    for p in range(0, partidas):
        golspartidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
    dados['gols'] = golspartidas[:]
    dados['total'] = sum(golspartidas)
    lista.append(dados.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(dados)
#print(lista)
print('-'*40)                              #cabeçalho
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)                               #cabeçalho
for k, v in enumerate(lista):               #printa o número do código do jogador (posição do dicionário na lista
    print(f'{k:>3} ', end='')
    for d in v.values():                    #Printa as informações do jogador que estão no diconário
        print(f'{str(d):<15}', end='')      #Parece que tem que converter os valores para string, por isso str(d). Se tiver dado numérico e não converter para string da erro.
    print('')
print('-'*40)
while True:
    busca = int(input('Mostrar dadosde qual jogador? (999 para encerrar): '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}: ')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-'*40)
print(' --Volte Sempre!')
#Pelo que eu entendi, nos dicionários não acumuam os valores como as listas. Em um laço infinito, a cada ve que você
#adiciona um novo valor no dicionário, ele é substituido. Então não faz muito sentido apagar os dados do dicionário
#a cada vez que vai realizar um loop para entrada de dados, pois eles serão substituídos