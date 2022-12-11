km = float(input('Quantidade de km percorrido '))
dias = int(input('Quantidade de dias que foi alugado '))
total = (dias * 60) + (km * 0.15)
print('A pagar pelos dias {:.2f}'.format(total))