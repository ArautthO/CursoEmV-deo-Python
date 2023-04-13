from time import sleep
saida = 0
while saida != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    saida = 0
    while saida != 4 and saida != 5:
        num3 = int(input('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
OPÇÕES:
[ 1 ] SOME OS NÚMEROS
[ 2 ] MULTIPLIQUE OS NÚMEROS
[ 3 ] NÚMERO MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'''))
        if num3 > 5:
            print('DIGITE UM NÚMERO VÁLIDO!')
            sleep(2)
        else:
            if num3 == 1:
                print('A soma dos números {} e {} é igual a {}'.format(num1, num2, (num1 + num2)))
                sleep(2)
            if num3 == 2:
                print('A Multiplicação dos númeors {} e {} é igual a {}'.format(num1, num2, (num1*num2)))
                sleep(2)
            if num3 == 3:
                if num1 > num2:
                    print('O maior número é {}'.format(num1))
                    sleep(2)
                else:
                    print('O maior número é {}'.format(num2))
                    sleep(2)
            if num3 == 4:
                saida = num3
                sleep(0.5)
            if num3 == 5:
                saida = 5
sleep(1)
print('Até mais!')
sleep(1)



