from random import randint
from time import sleep
cont = num = maq = soma = 0
while True:
    jog = str(input('Par ou ímpar? [P/I] ')).strip()
    maq = randint(0, 10)
    if jog in 'Ii':
        num = int(input('Seu número é: '))
        soma = num + maq
        print(f'Você jogou {num} e o Computador {maq}')
        sleep(0.5)
        print(f'O resultado deu {soma}')
        if soma % 2 == 0:
            print(f'{soma} é PAR!')
            sleep(0.5)
            print('Desculpe Você perdeu!')
            sleep(1)
            break
        else:
            print(f'{soma} é ÍMPAR!')
            sleep(0.5)
            print('PARABÉNS! Você GANHOU!')
            cont += 1
            sleep(1)
    elif jog in 'Pp':
        num = int(input('Seu número é: '))
        soma = num + maq
        print(f'Você jogou {num} e o Computador {maq}!')
        sleep(0.5)
        print(f'O Resultado deu {soma}!')
        if soma % 2 == 0:
            print(f'{soma} é PAR!')
            print('PARABÉNS! Você GANHOU!')
            cont += 1
            sleep(1)
        else:
            print(f'{soma} é ÍMPAR!')
            print('Desculpe você perdeu!')
            sleep(1)
            break
    else:
        print('Desculpe Não Entendi! Repita...')
        sleep(1)
print(f'Você teve {cont} vitórias Consecutivas!')