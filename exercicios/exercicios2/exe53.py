frase = str(input('Digite um frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('A palavra {} ao contrário é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo')
else:
    print('não temos um palíndromo')