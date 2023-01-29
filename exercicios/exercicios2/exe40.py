nota1 = float(input('Digite a nota 1 '))
nota2 = float(input('Digite a nota 2 '))
media = (nota1 + nota2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
if media >= 7:
    print('o aluno está aprovado')
elif 7 > media >= 5:
    print('o aluno está em recuperação')
else:
    print('o aluno está reprovado')