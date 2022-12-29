num1 = int(input('Digite o primeiro valor '))
num2 = int(input('Digite o segundo valor '))
if num1 > num2:
    print('O primeiro valor {}, é maior'.format(num1))
elif num1 < num2:
    print('O segundo valor {}, é maior'.format(num2))
else:
    print('Os dois valores são iguais')