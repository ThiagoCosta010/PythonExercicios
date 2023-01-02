preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção ? '))
if opcao == 1:
    total = preço - (preço * 10 / 100)
    print('Sua compra terá um desconto de 10% desconto, ficando {:.2f}R$ o total'.format(total))
elif opcao == 2:
    total = preço - (preço * 5 / 100)
    print('Sua compra terá um desconto de 5% desconto, ficando {:.2f}R$ o total'.format(total))
elif opcao == 3:
    parcelado = preço / 2
    print('Você pagara duas parcelas de R${}'.format(parcelado))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas ?'))
    juros = preço + (preço * 20 / 100)
    precoJuros = juros
    total = precoJuros / parcelas
    print('Sua compra será parcelado em {}x de R${:.2f} com JUROS'.format(parcelas, total))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço,juros))
else:
    print('Opção invalida')