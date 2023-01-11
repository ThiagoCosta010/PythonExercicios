from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(menor))