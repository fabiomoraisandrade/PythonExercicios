frase = input('Digite uma frase: ').strip().upper()
palavra = frase.split() #Dividir a frase eliminando os espaços entre as palavras
junto = ''.join(palavra) #Juntar para eliminar os espaços entre as palavras
inverso = ''
for letra in range(len(junto) - 1, -1, -1): #Fazendo o inverso da frase digitada sem os espaços
    inverso = inverso + junto[letra]
print('A frase que você digitou é {} e de trás pra frente é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
# Fazendo sem o for
#Basta escrever inverso = junto[::-1]

