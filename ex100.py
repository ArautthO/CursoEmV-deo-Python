from time import sleep
from random import randint


def sorteia(lista):
    print(f'Sorteando 5 valores... ', end='')
    for c in range(0, 5):
        sleep(.5)
        val = randint(1, 10)
        print(f'{val} ', end='')
        lista.append(val)
    sleep(.4)
    print('PRONTO!')
    sleep(1)


def somaPar(lista):
    par = 0
    for k in lista:
        if k % 2 == 0:
            par += k
    print(f'A soma dos Valores pares de {lista} é {par}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)

