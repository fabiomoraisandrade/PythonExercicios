print('{:=^40}'.format(' LOJAS ANDRADE '))
vp = float(input('Valor do produto: R$'))
print('''Condições de pagamento:
[ 1 ] À Vista (Dinheio ou Cheque)
[ 2 ] À Vista (Cartão)
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Informe a opção de pagamento: '))
if opção > 4 or opção == 0:
    print('Opção inválida. Tente novamente')
elif opção == 1:
    nv = vp * 0.9
    print('O valor a ser pago é R${:.2f}'.format(nv))
elif opção == 2:
    nv = vp * 0.95
    print('O valor a ser pago é R${:.2f}'.format(nv))
elif opção == 3:
    print('O valor a ser pago é o valor normal sem desconto, R${:.2f}'.format(vp))
    print('O valor de cada parcela é R${:.2f}'.format(vp/2))
else:
    t = int(input('Em quantas vezes você deseja parcelar? '))
    if t < 3:
        print('Opção inválida. Escolha uma nova forma de pagamento ou um número de parcelas maior que 3.')
    else:
        nv = vp * (1 + 0.2*t)
        p = nv / t
        print('O valor total do produto a ser pago em {} parcelas é R${:.2f}'.format(t, nv))
        print('O valor de cada parcela é {:.2f}'.format(p))



