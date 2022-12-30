from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano que você nasceu '))
idade = atual - nasc
if idade == 18:
    print('Você precisa se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda não precisa se alistar, falta {} anos'.format(saldo))
else:
    saldo = idade - 18
    print('Você já se alistou, {} anos atrás'.format(saldo))