n = input('Digite algo: ')
print ('O tipo é {}. É númerico? {}. É alfanumérico? {}. É alpha? {}. É ascii? {}. É decimal? {}. É digit? {}. É identifier? {}. É minusculo? {}. É printable? {}. É space? {}. É title? {}.'.format(type(n), n.isnumeric(), n.isalnum(), n.isalpha(), n.isascii(), n.isdecimal(), n.isdigit(), n.isidentifier(), n.islower(), n.isprintable(), n.isspace(), n.istitle()))
#A função input() retorna uma string.
#A função .isalnum() verifica se o input é alfanumerico (composto por numeros e letras)
#A função .isnumeric() verific se é possível converter o input em um numero do tipo primitivo inteiro(int)
