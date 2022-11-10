#print('Gerador de P.A')
#print('=-'*8)
#a1 = int(input('Primeiro termo: '))
#r = int(input('Razão: '))
#termo = a1
#c = 1
#while c <= 10:
#    print('{}, '.format(termo), end='')
#    termo = termo + r
#    c = c + 1
#print('FIM')
#opção = 0
#while opção != 2:
#    print('''Exibir mais números na P.A?
#    [ 1 ] SIM
#    [ 2 ] NÃO''')
#    opção = int(input('Informe uma opção: '))
#    if opção == 1:
#        p = int(input('Número de termos a mais a serem exibidos: '))
#        cont = 1
#        termo = a1 #Quando acabou o primeiro laço, a variável termo tem guardado na sua memória o último valor. Fazendo ele
#        while cont <= 10 + p: #ficar com o primeiro valor para mostrar toda a sequencia com os números a mais.
#            print('{}, '.format(termo), end='')#O problema é que se pedir para mostrar mais 2 números, ele vai mostrar a mesma
#            termo = termo + r#seqência de novo ao invés de somar mais 2 a anterior. Assim, teria que pedir pra mostrar mais 4.
#            cont = cont + 1
#    elif opção == 2:
#        print('Encerrando programa...')
#    else:
#        print('Opção inváida. Tente novamente')
#print('FIM')
print('Gerador de P.A')
print('=-'*8)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
termo = a1
t = 0
n = 10
while n != 0:
    t = t + n
    while c <= t:
        print('{}, '.format(termo), end='')
        termo = termo + r
        c = c + 1
    print('Pausa')
    n = int(input('Número de termos que serão exibidos a mais: '))
print('A progressão finalizou com {} termos exibidos'.format(t))


