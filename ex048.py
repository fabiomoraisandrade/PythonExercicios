s = 0
i = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1: #Condição para múltiplo de 3 e números ímpares respectivamente
        s = s + c #acumulador
        i = i + 1 #contador
print('O número de valores ímpares e múltiplos de 3 é {}. A soma de todos os valores ímpares múltiplos de 3 entre 0 e 500 é {}'.format(i, s))

#uma outra forma seria for c in range(1, 501, 2) para os numeros impares e colocar somente a condição if c % 3 ==0 para multiplos de 3


