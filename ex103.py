def ficha(nome='<desconhecido>', n=0):
    print(f'O jogador {nome} marcou {n} gols')


#programa principal
m = str(input('Nome do jogador: '))
nu = str(input('Número de gols: ')) #O número de gols tem que ser str, pois caso contrário, da erro ao ler uma entrada vazia
if nu.isnumeric():
    nu = int(nu)
else:
    nu = 0
if m.strip() == '':  #É necessário essa condição pois mesmo colocando a variável nome como opcional, se entrar os dados  como vazio, o valor opcional não é atribuído.
    ficha(n = nu)
else:
    ficha(m, nu)
