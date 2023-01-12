def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número inteiro válido!\033[m')
            #continue
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número real válido!\033[m')
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')
