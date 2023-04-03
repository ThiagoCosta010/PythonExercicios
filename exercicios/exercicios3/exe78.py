valores = []
maior = []
menor = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))

for pos, v in enumerate(valores):
    if v == max(valores):
        maior.append(pos)
    if v == min(valores):
        menor.append(pos)
print(f'O menor valor foi {min(valores)} na posição {menor}')
print(f'O menor valor foi {max(valores)} na posição {maior}')

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
