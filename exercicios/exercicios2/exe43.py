peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura '))
imc = peso / (altura ** 2)
print('Seu IMC é {}'.format(imc))
if imc < 18.5:
    print('Baixo peso')
elif imc < 25:
    print('Peso Normal')
elif imc < 30:
    print('Sobrepeso')
else:
    print('Obesidade')