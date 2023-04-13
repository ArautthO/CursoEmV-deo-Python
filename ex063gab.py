print('~'*22)
print('SEQUÊNCIA DE FIBONACCI')
print('~'*22)
elem = int(input('Quantos elementos quer ver? '))
num1 = 0
num2 = 1
num3 = 0
print('{} → {}'.format(num1, num2), end='')
cont = 3
while cont <= elem:
    num3 = num1 + num2
    print(' → {}'.format(num3), end='')
    num1 = num2
    num2 = num3
    cont += 1
print(' → FIM')

