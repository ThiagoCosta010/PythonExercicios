p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('fim')