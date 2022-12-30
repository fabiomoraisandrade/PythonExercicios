from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - nasc
cart = int(input('Carteira de Trabalho (Se não tiver, digite 0): '))
if cart != 0:
    dados['CTPS'] = cart
    contrat = int(input('Ano de contratação: '))
    dados['Contratação'] = contrat
    dados['Salário'] = float(input('Salário R$'))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (date.today().year - contrat))
else:
    dados['CTPS'] = cart
print('-'*30)
#print(dados)
for k, v in dados.items():
    print(f'  - {k} é {v}')

