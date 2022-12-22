velocidade = float(input('Qual a velocidade do carro ? '))
if velocidade <= 80:
    print('Não multado')
else:
    multa = (velocidade-80) * 7
    print('Multado, deve pegar uma multa de R${:.2f}'.format(multa))