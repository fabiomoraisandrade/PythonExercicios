n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Digite uma opção: '))
if opção == 1:
    print('O valor {} convertido para binário é: {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('O valor {} convertido para octal é: {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('O valor {} convertido para hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente')
#A resposta das conversões dão um termo de 0b para binário, 0o para octal e ox para hexadecimal. Usando a técnica de fatiamento
#começando a exibir o resultado a partir do 3 termo que é numerado como 2.