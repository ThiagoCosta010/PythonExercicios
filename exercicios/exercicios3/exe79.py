numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado ! não vou adicionar')
    resp = str(input('Quer continuar: [S/N] ? ')).strip().upper()[0]
    if resp in 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')
