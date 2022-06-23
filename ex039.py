from datetime import date
print('''Escolha uma das opções para seu sexo
[ 1 ] para sexo masculino
[ 2 ] para sexo feminino''')
opção = int(input('Digite uma opção: '))
if opção == 2:
    print('O sexo feminino não faz parte do programa de serviço militar')
elif opção == 1:
    nascimento = int(input('Informe seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - nascimento
    if idade < 18:
        print('Você ainda vai se alistar no serviço militar. Sua idade é {} e seu alistamento será em {}'.format(idade,
                                                                                                                 (
                                                                                                                             nascimento + 18)))
    elif idade == 18:
        print('Você está com 18 anos. É hora de se alistar')
    else:
        print('Você está com {} anos. Seu alistamento foi em {}'.format(idade, (nascimento + 18)))
else:
    print('Opção inválida. Tente novamente.')



