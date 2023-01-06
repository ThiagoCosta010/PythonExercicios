from datetime import date
atual = date.today().year
for c in range(1,8):
    idade = atual - ano
    ano = input('Em que ano {}ª a pessoa nasceu ? '.format(c))
    if(idade >= 18):
        qtd = ano
print('{} pessoas passaram dos 18')
print('fim')