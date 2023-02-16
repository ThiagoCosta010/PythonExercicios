total = maisDeMil = maisBarato = 0
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    continua = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    total += preco
    if preco >= 1000:
        maisDeMil += 1
    if continua == 'N':
        break
print(f'O total de compras foi R${total}')
print(f'Temos {maisDeMil} produtos custando mais de R$1000.00')
#print(f'O produto mais barato foi {produtoBarato} que custa {maisBarato}')
