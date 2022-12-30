from time import sleep
#Solução ruim (grande e tem problema se colocar uma contagem de 24 a 32 com passo de 6 pois os valores
#de a e b nunca serão iguais e o programa entrará em loop infinito
'''def contador(a, b, c):
    tot = a
    if c > 0:
        print(f'Contagem de {a} até {b} de {c} em {c}: ')
        if a > b:
            while tot != (b-c):
                tot = tot - c
                print(f'{tot+c} ', end='')
                sleep(0.5)
        elif a < b:
            while tot != (b+c):
                tot = tot + c
                print(f'{tot-c} ', end='')
                sleep(0.5)
    elif c < 0:
        print(f'Contagem de {a} até {b} de {-c} em {-c}: ')
        if a > b:
            c = c * (-1)
            while tot != (b-c):
                tot = tot - c
                print(f'{tot+c} ', end='')
                sleep(0.5)
        if a < b:
            c = c * (-1)
            while tot != (b+c):
                tot = tot + c
                print(f'{tot-c} ', end='')
                sleep(0.5)
    elif c == 0:
        c = 1
        print(f'Contagem de {a} até {b} de {c} em {c}: ')
        if a > b:
            while tot != (b-c):
                tot = tot - c
                print(f'{tot+c} ', end='')
                sleep(0.5)
        elif a < b:
            while tot != (b+c):
                tot = tot + c
                print(f'{tot-c} ', end='')
                sleep(0.5)
    print('FIM!')
    print()'''

def contador(a, b, c):
    if c < 0:
        c = c * (-1)
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}: ')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='')
            cont = cont + c
            sleep(0.5)
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            cont = cont - c
            sleep(0.5)
        print('FIM!')


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora e sua vez de oersonalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

