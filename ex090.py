aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-'*35)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
#print(f'   - Nome é igual a {aluno["nome"]}')
#print(f'   - Média é igual a {aluno["media"]}')
#print(f'   - Situação é igual a {aluno["situação"]}')
