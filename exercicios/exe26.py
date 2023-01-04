nome = str(input('Digte um frase ')).strip().upper()
print('a letra A aparece {} vezes na frase'.format(nome.count('A')))
print('a primeira letra A aparece na posição {}'.format(nome.find('A')+1))
print('a última letra A aparece na posição {}'.format(nome.rfind('A')+1))