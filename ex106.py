from time import sleep
#A variiável c é uma variável global. Ela pode ser declarada tanto aqui no início como lá no programa principal
c = ('\033[m',     # 0 - Sem cor
     '\033[30m',   # 1 - Branco
     '\033[31m',   # 2 - Vermelho
     '\033[32m',   # 3 - Verde
     '\033[33m',   # 4 - Amarelo
     '\033[34m',   # 5 - Azul
     '\033[35m',   # 6 - Roxo (magenta)
     '\033[36m',   # 7 - Azul marinho (ciano)
     '\033[37m')   # 8 - Cinza (cor padrão)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


#PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 5)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        #titulo(f'Acessando o manual do comando {comando}', 3) #Dá pra chamar essa função dentro da função ajuda
        ajuda(comando)
titulo('Até logo!', 2)