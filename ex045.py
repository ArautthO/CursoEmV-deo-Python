import random
from time import sleep
print('Vamos jogar JoKenPô?')
jog = int(input('Faça sua jogada!\n'+'*' * 20+'\n 1 => Pedra \n 2 => Papel \n 3 => Tesoura \n'+'*' * 20 + '\nQual é a sua jogada? '))
Pedra = 10
Papel = 20
Tesoura = 30
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
if jog == 1:
    comp = random.choice([Pedra, Papel, Tesoura])
    sleep(.5)
    if comp == 10:
        print('O computador jogou: Pedra!')
        sleep(1)
        print('Você empatou! Pedra empata com Pedra!')

    elif comp==20:
        print('O computador jogou: Papel!')
        sleep(1)
        print('Você Perdeu! Pedra perde para Papel!')
    else:
        print('O Computador jogou: Tesoura!')
        sleep(1)
        print('Você Ganhou! Pedra ganha de Tesoura!')
    sleep(1)
    '''    if (jog + comp) == 31:
        print('Você Ganhou! Pedra ganha de Tesoura!')
    elif(jog + comp) == 21:
        print('Você Perdeu! Pedra perde para Papel!')
    else:
        print('Você empatou! Pedra empata com Pedra!')'''
elif jog == 2:
    comp = random.choice([Pedra, Papel, Tesoura])
    if comp == 10:
        print('O Computador jogou: Pedra!')
        sleep(1)
        print('Você Ganhou! Papel ganha de Pedra!')
    elif comp == 20:
        print('O Computador jogou: Papel!')
        sleep(1)
        print('Você empatou! Papel empata com Papel!')
    else:
        print('O Computador jogou: Tesoura!')
        sleep(1)
        print('Você perdeu! Papel perde para Tesoura!')
    sleep(.5)
    '''    if (jog + comp) == 12:
        print('Você Ganhou! Papel ganha de Pedra!')
    elif(jog + comp) == 32:
        print('Você Perdeu! Papel perde para Tesoura!')
    else:
        print('Você empatou, Papel empata com Papel!')'''
elif jog == 3:
    comp = random.choice([Pedra, Papel, Tesoura])
    sleep(.5)
    if comp == 10:
        print('O Computador jogou: Pedra!')
        sleep(1)
        print('Você perdeu! Tesoura perde para Pedra!')
    elif comp == 20:
        print('O Computador jogou: Papel!')
        sleep(1)
        print('Você Ganhou! Tesoura ganha de Papel!')
    else:
        print('O Computador jogou: Tesoura!')
        sleep(1)
        print('Você Empatou! Tesoura empata com Tesoura!')
    sleep(.5)
    ''' if (jog + comp) == 23:
        print('Você Ganhou! Tesoura ganha de Papel!')
    elif(jog + comp) == 13:
        print('Você Perdeu! Tesoura perde para Pedra')
    else:
        print('Você empatou! Tesoura empata com Tesoura!')'''
else:
    print('Não Vale Roubar! Escolha uma das opções!')