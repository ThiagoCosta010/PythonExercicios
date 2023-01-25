salario = float(input('Digite seu salário '))
if salario > 1250:
    aumento = salario + (salario*0.1)
    print('Quem ganha R${} com o aumento agora ganha R${}'.format(salario, aumento))
else:
    aumento = salario + (salario*0.15)
    print('Quem ganha R${} com o aumento agora ganha R${}'.format(salario, aumento))
