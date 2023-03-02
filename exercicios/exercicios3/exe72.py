cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis' ,'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 10 '))
    if num < 0 or num > 20:
        print('Tente Novamente ', end='')
        num = int(input('Digite um número entre 0 e 10 '))
    print(f'Você digitou o número {cont[num]}')
    continuar = str(input('Quer continuar ? ')).strip().upper()
    if continuar == 'N':
        break
print('fim')
