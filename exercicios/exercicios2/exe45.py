from random import randint
from time import sleep
itens = ['pedra','papel','tesoura']
computador = randint(0, 2)
jogador = int(input('''Faça sua escolha 
[0] Pedra
[1] Papel
[2] Tesoura
'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('o computador jogou {}'.format(itens[computador]))
print('o jogador jogou {}'.format(itens[jogador]))
if jogador == 0: # Pedra
    if computador == 0:
        print('Empate!')
    elif computador == 1:
        print('Computador ganhou')
    else:
        print('O jogador ganhou')
elif jogador == 1: # Papel
    if computador == 0:
        print('O jogador ganhou')
    elif computador == 1:
        print('Empate!')
    else:
        print('Computador ganhou')
else: #Tesoura
    if computador == 0:
        print('Computador ganhou')
    elif computador == 1:
        print('O jogador ganhou')
    else:
        print('Empate!')

