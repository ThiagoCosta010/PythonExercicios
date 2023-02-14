print('-----------------')
print('CADASTRE A PESSOA')
print('-----------------')
total18 = homens = mulheres20 = 0
while True:
    idade = int(input('Idade '))
    sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    continuar = str(input('Quer continuar ? ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homens += 1
    if idade <= 20 and sexo == 'M':
        mulheres20 += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos')
