import math
co = float(input('cateto oposto '))
ca = float(input('cateto adjacente'))
hi = math.hypot(co, ca)
print('o valor da hipotenusa {:.2f}'.format(hi))