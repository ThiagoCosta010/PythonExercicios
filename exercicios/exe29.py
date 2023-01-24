v = float(input('Digite a velocidade do carro '))
if v <= 80:
    print('Não foi multado')
else:
    multa = (v - 80) * 7
    print('Você foi multado e pagara um multa de R${}'.format(multa))
