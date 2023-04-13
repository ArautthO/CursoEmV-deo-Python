term = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    print(term, end='')
    print(' > ' if cont < 9 else '', end='')
    term += raz
    cont += 1
