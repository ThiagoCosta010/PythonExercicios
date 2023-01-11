from random import randint
print('Sou seu computador...')
print('Acabei de pensar num número entre 0 e 10')
print('Será que você consegue adivinhar qual foi ?')
computador = randint(0,10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ? '))
    palpite += 1
    if jogador == computador:
        print('Parabéns você acertou!')
    else:
        if jogador > computador:
            print('Menos... tente outra vez')
            palpite += 1
        elif jogador < computador:
            print('Mais... tente outra vez')
            palpite += 1
print('Você palpitou {} vezes'.format(palpite))