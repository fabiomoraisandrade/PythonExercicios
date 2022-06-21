import math
da = float(input('Informe um ângulo em °: '))
r = math.radians(da)
ras = math.sin(r)
rac = math.cos(r)
rat = math.tan(r)
#ds = math.degrees(ras)
#dc = math.degrees(rac)
#dt = math.degrees(rat)
print('O valor do seno de {} é {}'.format(da, ras))
print('O valor do cosseno de {} é {}'.format(da, rac))
print('O valor da tangente de {} é {}'.format(da, rat))
#Não precisa converter o resultado do seno, cosseno e tangente pois o angulo já foi transformado em radianos e o seno de um angulo em radiano já vai dar o valor certo.



