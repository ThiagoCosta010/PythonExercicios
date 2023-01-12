n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))
opcao = 0
while opcao != 5:
    print(''' =============
[ 1 ] Somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programqa
    ''')
    opcao = int(input('Qual a sua opção ? '))
    if opcao == 1:
        soma = n1 + n2
        print('a soma é {}'.format(soma))
    elif opcao == 2:
        mult = n1 * n2
        print('a multiplicação é {}'.format(mult))
    elif opcao == 3:
        if n1 > n2:
            print('O maior valor é {}'.format(n1))
        else:
            print('O maior valor é {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite um valor '))
        n2 = int(input('Digite outro valor '))
print('fim')