def dobro(n=0, formato=False):
    res = n*2
    if formato is False:
        return res
    else:
        return moeda(res)


def metade(n=0, formato=False):
    res = n/2
    if formato is False:
        return res
    else:
        return moeda(res)


def aumentar(n=0, x=0, formato=False):
    res = n + n*(x/100)
    if formato is False:
        return res
    else:
        return moeda(res)


def diminuir(n=0, x=0, formato=False):
    res = n - n*(x/100)
    if formato is False:
        return res
    else:
        return moeda(res)


def moeda(preço=0, moeda='R$'):
    return str(f'{moeda}{preço:>.2f}'.replace('.', ','))


'''def resumo(preço=0, aumento=0, redução=0):
    dados = {}
    dados['Preço Analisado:'] = moeda(preço)
    dados['Dobro do Preço:'] = dobro(preço, True)
    dados['Metade do preço:'] = metade(preço, True)
    dados[f'{aumento}% de aumento:'] = aumentar(preço, aumento, True)
    dados[f'{redução}% de redução'] = diminuir(preço, redução, True)
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    for k, v in dados.items():
        print(f'{k:<20} {v}')
    print('-'*30)'''


def resumo(preço=0, aumento=0, redução=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}') #\t é para tabulação(alinhar certinho)
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, redução, True)}')
    print('-'*30)