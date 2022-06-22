cidade = str(input('Qual é a sua cidade? ')).strip().title()
cidsep = cidade.split()
print('A cidade começa com Santo? {}'.format('Santo' in cidsep[0]))

#Outra solução
'''cidade = str(input('Qual é a sua cidade? ')).strip()
print(cidade[:5].title() == 'Santo')'''





