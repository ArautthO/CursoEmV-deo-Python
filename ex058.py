from random import randint
from time import sleep
cont = 0
num = 0
sort = randint(1, 10)
while num != sort:
    num = int(input('Digite um número de 0 a 10: '))
    cont += 1
    if num > 10:
        print('Digite um número válido!')
    else:
        sort = randint(0, 10)
        if num != sort:
            print('O Número digitado foi {}'.format(num))
            sleep(0.5)
            print('o Número pensado foi {}!'.format(sort))
            sleep(1)
            print('Você Errou!')
print('O número digitado foi {}!'.format(num))
sleep(0.5)
print('O Número pensado foi {}!'.format(sort))
sleep(1)
print('Parabéns! Você acertou!')
sleep(0.5)
print('Você precisou de {} tentativas!'.format(cont))
