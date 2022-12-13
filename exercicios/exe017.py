'''catOpo = float(input('cateto oposto: '))
catAdj = float(input('cateto adjacente '))
hi = (catOpo**2 + catAdj**2) ** (1/2)
print('total é {:.2f}'.format(hi))'''

import math
catOpo = float(input('cateto oposto: '))
catAdj = float(input('cateto adjacente '))
hi = math.hypot(catOpo,catAdj)
print('A hipotenusa vai medir {:.2f}'.format(hi))

