from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8, 1):
    ano = int(input('Em que ano a {}ª pessoa nasceu'.format(pess)))
    idade = atual - ano
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
print('fim')
