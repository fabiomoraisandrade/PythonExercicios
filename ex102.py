def fatorial(m, show=False):
    """
    ->Calcula o fatorial de um número m.
    :param m:Número a ser calculado.
    :param show:(opcional) True: mostra a conta, False: Mostra só o resultado.
    :return:Retorna o valor do fatorial do número m.
    """
    f = 1
    for c in range(m, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f = f * c
    return f

#PROGRAMA PRINCIPAL
print(fatorial(5, True))
