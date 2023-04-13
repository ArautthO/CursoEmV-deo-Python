'''from math import factorial'''
num = int(input('Digite um número para calcular seu Fatorial: '))
'''fac = factorial(num)
print('o Fatorial de {} é {}'.format(num, fac))'''
cont = num
fat = 1
print('Calculando {}!'.format(cont))
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))