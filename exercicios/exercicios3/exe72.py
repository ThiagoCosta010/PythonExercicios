cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis' ,'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamente', end=' ')
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {cont[num]}')
    continuar = str(input('Quer continuar [S/N] ?')).strip().upper()[0]
    if continuar == 'N':
        break
print('fim')