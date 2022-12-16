import math
angulo = float(input('Digite o angulo '))
seno = math.sin(math.radians(angulo))
print('O angulo {} tem o seno {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo {} tem o cosseno {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem a tangente {:.2f}'.format(angulo, tangente))
