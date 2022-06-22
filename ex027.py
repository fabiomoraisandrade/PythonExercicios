nome = str(input('Digite seu nome completo: ')).strip().title()
n = nome.split()
print('Primeiro nome: {}'.format(n[0]))
print('Ultimo nome: {}'.format(n[len(n)-1]))


