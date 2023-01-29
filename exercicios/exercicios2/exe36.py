casa = float(input('Qual o valor da sua casa ? '))
salario = float(input('Qual o seu sálario ? '))
anos = int(input('Quantos anos de financiamento ? '))
prestacao = casa / (anos*12)
minimo = salario * 30/100
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo aceito')
else:
    print('Empréstimo negado')