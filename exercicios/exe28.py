from random import randint
from time import sleep
n1 = randint(0,5)
chute = int(input('Digite um número entre 0 e 5 '))
print('PROCESSANDO...')
sleep(2)
if chute == n1:
    print('Acertou')
else:
    print('errou, era {}'.format(n1))