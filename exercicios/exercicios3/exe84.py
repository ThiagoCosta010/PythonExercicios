lista = []
princ = []
mai = men = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = lista[1]
    else:
        if lista[1] > mai:
            mai = lista[1]
        if lista[1] < men:
            men = lista[1]
    princ.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'Ao, todos você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
