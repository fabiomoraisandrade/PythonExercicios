def maior(*num):
    mai = 0
    for c, v in enumerate(num):
        if c == 0:
            mai = v
        else:
            if v > mai:
                mai = v
    print(f'Analisando os valores passados...')
    for c in num:
        print(f'{c} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor é {mai}')

#PROGRAMA PRINCIPAL
maior(5, 3, 7, 10)
maior(3, 4)
maior()
