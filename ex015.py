q = float(input('Informe a quantidade de quilometros rodados : '))
d = int(input('Informe o número de dias que o carro foi alugado: '))
p = d*60 + q*0.15
print('O aluguel do carro é no valor de R${:.2f}'.format(p))
