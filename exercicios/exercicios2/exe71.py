valor50 = valor10 = 0
while True:
    sacar = float(input('Que valor você quer sacar ? '))
    if sacar >= 50:
        valor50 = sacar / 50
        if sacar >= 10:
            valor10 = sacar / valor50
    if sacar == 0:
        break
print(f'Total de {valor50} cédulas de R$50')
print(f'Total de {valor10} cédulas de R$10')