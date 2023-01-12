def notas(*s, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos
    :param s: Notas dos alunos (aceita várias)
    :param sit: Mostra a situação do aluno
    :return: Retorna um dicionário com informações do aluno
    """
    n = {}
    n['total'] = len(s)
    n['maior'] = max(s)
    n['menor'] = min(s)
    n['media'] = sum(s)/len(s)
    if sit == True:
        if n['media'] >= 7:
            n['situação'] = 'BOA'
        elif n['media'] >= 5:
            n['situação'] = 'RAZOÁVEL'
        else:
            n['situação'] = 'RUIM'
    return n


#PROGRAMA PRINCIPAL
resp = notas(10, 7, 8, 5, sit=True)
print(resp)
help(notas)
