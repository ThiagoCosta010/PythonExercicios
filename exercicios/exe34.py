salario = float(input('Digite seu salário '))
if salario > 1250:
    aumento = salario + (salario*0.1)
    print('Seu novo salário vai ser {}'.format(aumento))
else:
    aumento = salario + (salario*0.15)
    print('Seu novo salário vai ser {}'.format(aumento))
