num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} \033[m'.format(c), end='')
if tot == 2:
    print('\no valor é primo')
else:
    print('\nnão é primo')
print('o valor foi dívisível {} vezes'.format(tot))
