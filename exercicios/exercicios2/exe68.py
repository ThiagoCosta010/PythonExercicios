from random import randint
print('VAMOS JOGAR PAR OU IMPAR')
cont = venceu = 0
while cont <= 3:
    computador = randint(0, 11)
    valor = int(input('Diga um valor'))
    parImpar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    cont += 1
    print(f'Você jogou {valor} e o computador {computador}')
    soma = valor + computador
    if soma % 2 == 0:
        print('DEU PAR')
        if parImpar == 'P':
            print('Você venceu')
            venceu += 1
        else:
            print('Você perdeu')
    else:
        print('DEU IMPAR')
        if parImpar == 'I':
            print('Você venceu')
        else:
            print('Você perdeu')
print(f'Você ganhou um total de {venceu} rodadas')