from time import sleep
opção = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while opção != 5:
    print('''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    OPÇÕES:
    [ 1 ] SOME OS NÚMEROS
    [ 2 ] MULTIPLIQUE OS NÚMEROS
    [ 3 ] NÚMERO MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n''')
    opção = int(input('>>> Qual é a sua opção: '))
    if opção == 1:
        sleep(0.5)
        print('O Resultado de {} + {} é {}'.format(n1, n2, (n1+n2)))
        sleep(1)
    elif opção == 2:
        sleep(0.5)
        print('O Resultado de {} x {} é {}'.format(n1, n2, (n1*n2)))
        sleep(1)
    elif opção == 3:
        sleep(0.5)
        if n1 > n2:
            print('O número maior é {}'.format(n1))
        elif n2 > n1:
            print('O número maior é {}'.format(n2))
        else:
            print('Os números são iguais!')
        sleep(1)
    elif opção == 4:
        sleep(0.5)
        print('Digite os número novamente!')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opção == 5:
        sleep(0.5)
        print('Finalizando...')
        sleep(1)
    else:
        sleep(0.5)
        print('Opção inválida! Digite Novamente!')
        sleep(1)
