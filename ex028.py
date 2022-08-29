from random import randint
from time import sleep
num = int(input('A máquina pensou em um número de 1 a 5,\n'
                'Tente acertar esse número: '))
sort = randint(1, 5)
print ('PROCESSANDO...')
sleep(1)
if num == sort:
    print('Você é demais! Acertou o número pensado!')
else:
    print('Infelizmente não foi desta vez que você acertou! Tente novamente!')
print('O número pensado foi {}'.format(sort))

