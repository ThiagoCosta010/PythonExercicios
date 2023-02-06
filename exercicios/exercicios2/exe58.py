from random import randint
print(''' Sou seu computador...
 Acabei de pensar em um número entre 0 e 10.
 Será que você consegue adivinhar qual foi ?''')
computador = randint(0, 10)
tentantivas = 0
acertou = False
while not acertou:
    palpite = int(input('Qual é o seu palpite ? '))
    tentantivas += 1
    if palpite == computador:
        acertou = True
        print('Parabéns você adivinhou')
    elif palpite > computador:
        print('Menos...Tente mais uma vez ')
    else:
        print('Mais...Tente mais uma vez ')
print('Você teve {} tentativas'.format(tentantivas))