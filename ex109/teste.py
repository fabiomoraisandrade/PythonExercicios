from ex109 import moeda

#PROGRAMA PRINCIPAL
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% temos {moeda.diminuir(p, 13, True)}')

# Tirando o moeda.moeda(moeda.metade(p)) do ex108 pois fica dificil de entender
