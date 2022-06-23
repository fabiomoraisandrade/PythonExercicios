n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))
if n1 > n2:
    print('O maior número é {}'.format(n1))
    print('O menor número é {}'.format(n2))
elif n2 > n1:
    print('O maior número é {}'.format(n2))
    print('O menor número é {}'.format(n1))
else:
    print('Não existe valor maior, os dois são iguais.')
#Pode ser colocado mais uma condição elif no lugar do else