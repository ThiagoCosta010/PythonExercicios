v = float(input('Digite a velocidade do carro '))
if v <= 80:
    print('Diriga com cuidado')
else:
    multa = (v-80) * 7
    print('Multado! Excedeu o limite permitido que é de 80km/h \n Pagara uma multa de {}'.format(multa))