salario = float(input('Qual o salário do funcionário R$'))
aumento = salario + (salario * 0.15)
print('Seu salario de R${:.f2} com o aumento de 15% fica R${:.2f}'.format(salario, aumento))