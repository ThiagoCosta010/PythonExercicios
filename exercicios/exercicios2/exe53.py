frase = str(input('Digite um frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('não tem um palíndromo')