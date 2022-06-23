c1 = float(input('Comprimento reta 1: '))
c2 = float(input('Comprimento reta 2: '))
c3 = float(input('Comprimento reta 3: '))
if c1 < (c2 + c3) and c2 < (c1 + c3) and c3 < (c1 + c2):
    print('Os segmentos podem formar um triângulo')
else:
    print('Os segmentos não podem formar um triângulo')
