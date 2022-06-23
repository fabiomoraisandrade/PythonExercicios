n = float(input('Qual é a distância da viagem em km? '))
if n<=200:
    p = n*0.5
    print('O preço da sua viagem é {:.2f}.'.format(p))
else:
    p = n*0.45
    print('O preço da sua viagem é {:.2f}.'.format(p))
#Não é necessário criar uma variável diferente nos blocos de if e else. Pode ser a mesma variável p, pois os dois bloos não acontessem simultaneamente.
