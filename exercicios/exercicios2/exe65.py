opcao = 's'
soma = quant = media = maior = menor = 0
while opcao not in 'Nn':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar [S/N]?')).upper().split()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior foi {} e o menor foi {}'.format(maior, menor))