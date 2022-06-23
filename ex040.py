n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2)/2
if n1 > 10 or n2 > 10:
    print('Valor inválido. Tente novamente')
elif m < 5:
    print('Reprovado. Sua média foi {:.1f}'.format(m))
    print('Estude mais')
elif m >= 5 and m < 7:
#7 > m >= 5 também da certo
    print('Recuperação. Sua média foi {:.1f}'.format(m))
else:
    print('Aprovado! Sua média foi {:.1f}'.format(m))


