n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))
opcao = 0
while opcao != 5:
    print('''
    
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa
    ''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é o {}'.format(n1))
        else:
            print('O maior número é o {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite um valor '))
        n2 = int(input('Digite outro valor '))
    elif opcao >= 6:
        print('Opção inválida')
    elif opcao == 5:
        print('fim')
