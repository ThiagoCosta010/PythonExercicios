onepiece = []
sagas = {'arco': 'east blue', 'vilão': 'Arlong'}
sagas2 = {'arco': 'alabast', 'vilão': 'Crocodile'}
onepiece.append(sagas)
onepiece.append(sagas2)
print(onepiece[0]['arco'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()