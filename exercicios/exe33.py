a = int(input('Primeiro valor '))
b = int(input('Segundo valor '))
c = int(input('Terceiro valor '))
# Verificar o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))

