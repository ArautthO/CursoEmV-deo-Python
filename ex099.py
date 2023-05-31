from time import sleep


def maior(* num):
    pos = g = 0
    print('=-=' * 15)
    print('Analisando os valores passados...')
    while pos < len(num):
        sleep(.4)
        print(f'{num[pos]} ', end='')
        if pos == 0:
            g = num[0]
        else:
            if g < num[pos]:
                g = num[pos]
        pos += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor destes é o {g}.')


maior(2, 9, 4, 5, 7, 1)
sleep(2)
maior(4, 7, 0)
sleep(2)
maior(1, 2)
sleep(2)
maior(6)
sleep(2)
maior()

