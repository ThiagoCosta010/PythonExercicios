'''distancia = float(input('Distancia da viagem em Km '))
if distancia <= 200:
    preco = distancia * 0.50
    print('Preço: R${}'.format(preco))
else:
    preco = distancia * 0.45
    print('Preço: R${}'.format(preco))'''

distancia = float(input('Distancia da viagem em Km '))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será {:.2f}'.format(preco))