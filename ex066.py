# O exercicio pede para mostrar a soma. Para isso, basta exibir na tela a soma. Fiz com a média para variar um pouco
s = 0
i = 0
while True:
    n = int(input('Informe um número inteiro (Digite 999 para parar): '))
    if n == 999:
        break
    s = s + n
    i = i + 1
    m = s / i #Dessa vez o cálculo da média tem que ficar no laço pois se o primeiro valor informado for o 999, o calculo da media seria 0/0
print(f'A quantida de números inseridos é {i} e sua média é {m:.2f}.')
