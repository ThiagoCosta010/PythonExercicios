from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu ?'))
idade = atual - ano
print('Quem nasceu em {} tem {} anos'.format(ano, idade))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    falta = 18 - idade
    alista = atual + falta
    print('Falta {} anos para o seu alistamento'.format(falta))
    print('Seu alistamento será em {}'.format(alista))
elif idade > 18:
    falta = idade - 18
    alista = atual - falta
    print('Você já deveria ter se alistado há {} anos'.format(falta))
    print('Seu alistamento foi em {}'.format(alista))