from time import sleep
print('Para uma progressão aritimética:')
term = int(input('Digite o termo: '))
raz = int(input('Digite a razão: '))
cont= 1
ded = 0
while cont != 0:
    while cont <= 10:
        print(term, end='-> ')
        term += raz
        cont += 1
    ded = int(input('\nQuantos termos mais: '))
    if ded == 0:
        cont = 0
    else:
        cont = 11 - ded
sleep(1)
print('Até mais!')
sleep(1)