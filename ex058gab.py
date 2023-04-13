from random import randint
from time import sleep
sort = randint(0, 10)
acertou = False
cont = 0
print('Eu pensei em um número entre 0 e 10, consegue acertar?')
while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    cont += 1
    if sort == palpite:
        acertou = True
    else:
        if sort > palpite:
            sleep(1)
            print('Errou! é mais')
        else:
            sleep(1)
            print('Errou! é menos!')
print('Parabéns! Você acertou! E precisou de {} palpites para isso!'.format(cont))