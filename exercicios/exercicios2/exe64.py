num = cont = soma = 0
num = float(input('Digite um número [999 para parar]'))
while num != 999:
    soma += num
    num = float(input('Digite um número [999 para parar]'))
    cont += 1
print('Você digitou {} números e a soma é: {} '.format(cont, soma))