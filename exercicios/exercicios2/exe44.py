preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção ? '))
if opcao == 1:
    desconto = preço - (preço * 10/100)
    print('Sua compra com 10% de desconto fica R${}'.format(desconto))
elif opcao == 2:
    desconto = preço - (preço * 10/50)
    print('Sua compra com 5% de desconto fica R${}'.format(desconto))
elif opcao == 3:
    parcelado = preço/2
    print('Você pagara duas parecelas de R${}'.format(parcelado))
elif opcao == 4:
    parcela = int(input('Quantas vezes vai parcelar ?'))
    juros = preço + (preço * 20/100)
    parcelado = juros/parcela
    print('Sua compra será parecelada em {}x de R${} com juros'.format(parcela, parcelado))
    print('Sua compra de R${} fica R${}'.format(preço, juros))
else:
    print('Opção inválida')