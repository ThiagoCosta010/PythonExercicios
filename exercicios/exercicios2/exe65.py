opcao = 's'
soma = quant = media = maior = menor = 0
while opcao not in 'Nn':
    num = float(input('Digite um número: '))
    opcao = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
