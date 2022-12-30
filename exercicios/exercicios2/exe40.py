nota1 = float(input('Digite a nota 1 '))
nota2 = float(input('Digite a nota 2 '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Com as notas {} e {} sua média é {}, você está REPROVADO'.format(nota1, nota2, media))
elif media >= 5 and media < 7:
    print('Com as notas {} e {} sua média é {}, você está em RECUPERAÇÃO'.format(nota1, nota2, media))
else:
    print('Com as notas {} e {} sua média é {}, você está APROVADO'.format(nota1, nota2, media))
