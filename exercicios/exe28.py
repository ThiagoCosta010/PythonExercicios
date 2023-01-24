from random import randint
from time import sleep
computador = randint(0, 5)
num = int(input('Em que número eu pensei ? '))
print('PROCESSANDO...')
sleep(2)
if num == computador:
    print('Parabéns, você acertou')
else:
    print('Errou, eu pensei no {}'.format(computador))
