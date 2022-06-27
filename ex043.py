p = float(input('Informe seu peso (kg): '))
h = float(input('Informe sua altura (m): '))
imc = p/(h**2)
print('Seu índice de massa copórea é: {:.2f}.'.format(imc))
if imc < 18.5:
    print('Status: Abaixo do peso.')
elif imc < 25:
    print('Status: Peso ideal.')
elif imc < 30:
    print('Status: Sobrepeso.')
elif imc < 40:
    print('Status: Obesidade')
else:
    print('Status: Obesidade mórbida')
