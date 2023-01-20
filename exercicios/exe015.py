dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos km rodados ? '))
aluguel = (km*0.15) + (60*dias)
print('O total a pagar é R${}'.format(aluguel))
