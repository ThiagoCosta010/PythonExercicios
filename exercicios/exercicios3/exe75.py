num = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
      print(f'O valor 3 apareceu na posição {num.index(3)+1}º')
else:
      print('O valor 3 não apareceu em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for c in num:
      if c % 2 == 0:
            print(c, end=' ')
