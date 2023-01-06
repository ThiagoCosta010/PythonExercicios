numero = int(input('Digite um número '))
for c in range(0, 11, 1):
    soma = numero * c
    print('{} X {} = {}'.format(numero, c, soma))