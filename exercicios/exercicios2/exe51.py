termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(termo, razao*10, razao):
    print('->',c, end=' ')
print('-> ACABOU')