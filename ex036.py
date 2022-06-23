casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Tempo de pagamento em anos: R$'))
prestacao = casa / (anos * 12)
if prestacao > salario * 0.3:
    print('Empréstimp negado! O valor da prestação (R%{:.2f}) excedeu 30% do salário'.format(prestacao))
else:
    print('Empréstimo aprovado! O valor de cada prestação é R%{:.2f}'.format(prestacao))
