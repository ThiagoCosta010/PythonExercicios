from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opcões: 
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='* 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='* 11)
if computador == 0: # PEDRA
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('Jogada inválida!')
elif computador == 1: # PAPEL
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador vence')

    else:
        print('Jogada inválida!')

elif computador == 2: # TESOURA
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
