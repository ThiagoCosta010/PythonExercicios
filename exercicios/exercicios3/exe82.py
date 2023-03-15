num = []
impar = []
par = []
while True:
    num.append(int(input('Digite um número ')))
    resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {num}')
print(f'Lista de valores impares: {impar}')
print(f'Lista de valores pares: {par}')

