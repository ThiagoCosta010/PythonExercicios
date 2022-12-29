casa = float(input('Qual o valor da sua casa ? '))
salario = float(input('Qual o seu sálario ? '))
anos = int(input('Quantos anos de financiamento ? '))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos a prestração será {} '.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo não pode ser concedido')