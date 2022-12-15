exp = str(input('Digite  uma expressão: '))
pilha = []
for simb in exp:
    if simb == '(':            #Para cada parenteses abrindo que for encontrado na expressão, ele vai ser adicionado
        pilha.append('(')      #na lista pilha
    elif simb == ')':          #Para cada parenteses fechando encontrado na expressão, precisa comparar com a quantidade
        if len(pilha) > 0:     #de parenteses abrindo que foi encontrado na expressão que estão armazenados na lista pilha.
            pilha.pop()        #Se tiver parenteses abrindo na lista pilha, remove-se o último parenteses abrindo da lista pilha
        else:                  #o que significa que um par de parenteses abrindo e fechando foi encontrado e removido.
            pilha.append(')')  #Se não tiver parenteses abrindo na lista pilha, ou seja, se ela estiver vazia, adiciona-se um
            break              #parenteses fechando na pilha e para o laço, pois significa que existe mais parenteses fechando
if len(pilha) == 0:            #do que abrindo.
    print('Expressão válida')  #Dessa forma, se o número de caracteres da lista pilha for maior do que 0, existe um parenteses
else:                          #fechando que não encontrou seu par abrindo, significando que a expressão está incorreta.
    print('Expressão inválida')
