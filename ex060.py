num = int(input('Digite um numero: '))
fat = num
cont = num
print('Calculando {}! ='.format(cont))
while cont != 1:
    print(cont, end=' x ')
    cont -= 1
    fat = (fat*cont)
print('1')
print(fat)