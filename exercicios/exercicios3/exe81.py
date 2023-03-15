valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Você digitou {len(valores)}')
valores.sort()
valores.reverse()
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 não foi encontrado na lista')