def voto(n):
    from datetime import date #Colocando a importação na função economiza memória pois ela só entrará em execução quando a função for chamada
    idade = date.today().year - n
    if idade < 16:
        return str(f'Com {idade} anos: NÃO VOTA ')
    elif 16 <= idade < 18 or idade > 65:
        return str(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return str(f'Com {idade} anos: VOTO OBRIGATÓRIO')


#PROGRAMA PRINCIPAL
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))