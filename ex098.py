from time import sleep


def contador(a, b, c):
    print('=-=' * 15)
    print(f'Contagem de {a} até de {b} em {c}:')
    sleep(2.5)
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='')
            cont += c
            sleep(0.5)
        print('FIM!')
        print()
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            cont -= c
            sleep(0.5)
        print('FIM!')
        print()
    print('=-=' * 15)


#programa principal
print(f'PRIMEIRA CONTAGEM:')
contador(1, 10, 1)
sleep(1)
print(f'SEGUNDA CONTAGEM:')
contador(10, 0, 2)
print(f'TERCEIRA CONTAGEM:')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)