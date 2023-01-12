from ex108 import moeda

#PROGRAMA PRINCIPAL
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(p, 13))}')

# O moeda.moeda(p) primeiro chama o módulo que contem as funções moeda e depois a função moeda que formata o preço
# O moeda.moeda(moeda.metade(p)) chama o módulo que tem a função moeda para formatar o preço da função que irá dobrar, aumentar, reduzir ou dividir
