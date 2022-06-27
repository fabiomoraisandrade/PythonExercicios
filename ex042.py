r1 = float(input('Digite o comprimento do primeiro segmento de reta: '))
r2 = float(input('Digite o compprimento do segundo segmento de reta: '))
r3 = float(input('Digite o comprimento do terceiro segmento de reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    if r1 == r2 == r3:
        print('O triângulo formado é EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('O triângulo formado é ISÓSCELES.')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado é ESCALENO.')
else:
    print('Não é possível formar um triângulo.')




