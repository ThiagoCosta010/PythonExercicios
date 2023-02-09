p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p1
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        cont += 1
        termo += r
    print('PAUSA')
    mais = int(input('Quantos termos a mais quer mostrar ?'))
print('Progressão finalizada com {} termos mostrados'.format(total))
