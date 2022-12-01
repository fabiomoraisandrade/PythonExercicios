palavras = ('fabio', 'aprender', 'programar', 'estudos', 'mouse', 'computador')
for c in palavras: #c é a variável em cada posição da tupla palavra
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

