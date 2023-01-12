def leiadinheiro(msg):
    ok = False
    while not ok:
        p = str(input(msg)).strip().replace(',', '.')
        if p.isalpha() or p == '':
            print(f'\033[31mERRO!:"{p}" é um preço inválido\033[m')
        else:
            ok = True
            return float(p)
