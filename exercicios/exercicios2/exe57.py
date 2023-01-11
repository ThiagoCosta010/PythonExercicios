sexo = str(input('Qual o seu sexo ? [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido, escolha seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso '.format(sexo))