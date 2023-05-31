from random import randint
from time import sleep
mega = list()
cartão = list()
num = 0
print('=-='*8)
print('{:^25}'.format('MEGA SENA DA VIRADA'))
print('=-='*8)
jogos = int(input('Quantos jogos você quer? '))
print(f'SORTEANDO JOGOS...')
sleep(1)
for c in range(0, jogos):
    for d in range(0, 6):
        num = randint(1, 60)
        if num not in mega:
            mega.append(num)
        else:
            d = -1
    mega.sort()
    print(f'Jogo {c+1}: {mega}')
    cartão.append(mega[:])
    sleep(.5)
    mega.clear()
sleep(1)
print('=-=', 'BOA SORTE!', '=-=')