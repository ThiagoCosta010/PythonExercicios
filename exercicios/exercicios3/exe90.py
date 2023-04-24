alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = int(input(f'Media do {alunos["nome"]}: '))
if alunos['media'] > 7:
    alunos['situacao'] = 'Aprovado'
elif alunos['media'] < 3:
    alunos['situacao'] = 'Reprovado'
else:
    alunos['situacao'] = 'Recuperação'
print('-=' * 30)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
    