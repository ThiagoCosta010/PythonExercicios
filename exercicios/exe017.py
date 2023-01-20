import math
co = float(input('Valor do cateto oposto '))
ca = float(input('Valor do cateto adjacente '))
hipo = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hipo))