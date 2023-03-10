valores = []
maior = []
menor = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))

for posicao, v in enumerate(valores):
    if v == max(valores):
        maior.append(posicao)
    if v == min(valores):
        menor.append(posicao)
print(f'O mais valor foi {max(valores)} na posição {maior}')
print(f'O mais valor foi {min(valores)} na posição {menor}')

#for c in range(0, 5):
#    valores.append(int(input(f'Digite um valor na posição {c}: ')))
#    if c == 0:
#        maior = menor = valores[c]
#   else:
#        if valores[c] > maior:
#            maior = valores[c]
#        if valores[c] < menor:
#            menor = valores[c]
#print(f'maior valor foi {maior} nas posições ', end='')
#for i, v in enumerate(valores):
#    if v == maior:
#        print(f'{i}...', end='')
#print()
#print(f'menor valor foi {menor} nas posições ', end='')
#for i, v in enumerate(valores):
#    if v == menor:
#        print(f'{i}...', end='')
#print()
