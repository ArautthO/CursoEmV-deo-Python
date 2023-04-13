from time import sleep
primeiro = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
term = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(term), end='')
        print(' > ' if cont <= total - 1 else '', end='')
        term += raz
        cont += 1
    sleep(0.5)
    print('\nPausa!')
    sleep(0.5)
    mais = int(input('Deseja quantos mais? '))
    sleep(1)
print('O total de termos vistos é {}'.format(cont-1))
sleep(2)