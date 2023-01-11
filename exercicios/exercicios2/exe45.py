from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Sua opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA 
''')
jogador = int(input('Qual a sua escolha? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('O computor jogou {} '.format(itens[computador]))
print('o jogador jogou {} '.format(itens[jogador]))
if jogador == 0 : # PEDRA
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('Computador ganhou')
    elif computador == 2:
        print('Jogador jogou')
elif jogador == 1: # PAPEL
    if computador == 0:
        print('jogador ganhou')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('computador ganhou')
else: # TESOURA
    if computador == 0:
        print('computador ganhou')
    elif computador == 1:
        print('jogador ganhou')
    elif computador == 2:
        print('EMPATE')