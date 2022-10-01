from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-='*11)
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jog]))
print('-='*11)
if comp == 0:
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('GANHOU!')
    elif jog == 2:
        print('PERDEU!')
    else:
        print('JOGADA INVÁLIDA! Tente Novamente!')
elif comp == 1:
    if jog == 0:
        print('PERDEU!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('GANHOU!')
    else:
        print('JOGADA INVÁLIDA! Tente Novamente!')
else:
    if jog == 0:
        print('GANHOU!')
    elif jog == 1:
        print('PERDEU!')
    elif jog == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INVÁLIDA! Tente Novamente!')