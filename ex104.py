def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\33[31mErro! Digite um número inteiro válido\33[m')
        if ok == True:
            break
    return valor

#PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitr o número {n}')
