distancia = float(input('Qual a distãncia da sua viagem '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
'''if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('E o preço da sua passagem será R${}'.format(valor))'''
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será R${}'.format(preco))