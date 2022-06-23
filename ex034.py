s = float(input('Qual o seu salário? '))
if s > 1250:
    ns = s*1.1
    print('Seu novo salário é {}'.format(ns))
else:
    ns = s*1.15
    print('Seu novo salário é {}'.format(ns))
