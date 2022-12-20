frase = str(input('Digite um nome completo ')).strip().lower()
print('A letra a aparece {} vezes'.format(frase.count('a')))
print('A letra a apareceu na posição {}'.format(frase.find('a') + 1))
print('A última letra a apareceu na posição {}'.format(frase.rfind('a')+1))