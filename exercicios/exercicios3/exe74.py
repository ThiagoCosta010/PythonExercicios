from random import randint
valores = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os valores sorteados foram: ', end='')
for n in valores:
    print(f'{n} ', end='')
print(f'\n o maior valor sorteado foi {max(valores)}')
print(f'o menor valor sorteado foi {min(valores)}')
