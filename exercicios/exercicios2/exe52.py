numero = int(input('Digite um número: '))
for c in range(1, numero+1):
    if(numero % c == 0):
        print('é primo', c)
    else:
        print('não é primo', c)
# print(c, end='')
print('fim')