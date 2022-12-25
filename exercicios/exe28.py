from random import randint
from time import sleep
num = randint(0, 5)
print('-=-' * 20)
chute = int(input('Digite um número entre 0 e 5 '))
print('PROCESSANDO...')
sleep(2)
if chute == num:
    print('Você ganhou!!')
else:
    print('Você errou, o número era {}'.format(num))