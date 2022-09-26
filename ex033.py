num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))
if num1 > num2:
    if num1 > num3:
        print('O número maior é {}'.format(num1))
        if num2 > num3:
            print('O número menor é {}'.format(num3))
        else:
            print('O numero menor é {}'.format(num2))
    else:
        print('O numero {} é o maior'.format(num3))
        print('O número {} é o menor'.format(num2))
else:
    if num2 > num3:
        print('O numero maior é {}'.format(num2))
        if num1 > num3:
            print('O número menor é {}'.format(num3))
        else:
            print('O numero menor é {}'.format(num1))
    else:
        print('O numero maior é {}'.format(num3))
        print('O número menor é {}'.format(num1))

