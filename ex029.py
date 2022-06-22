v = float(input('Qual a velocidade do carro? '))
if v>80:
    m = (v-80)*7
    print('Você foi multado. O alor da multa é {}'.format(m))
else:
    print('A velocidade não está acima do limite de 80km/h')
