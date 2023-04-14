while True:
    num = int(input('Digite um numero pra ver sua tabuada: '))
    if num < 0:
        print('Finalizando...')
        break
    print('=-='*5)
    for cont in range(1, 11):
        print(f'{num:2} x {cont:2} = {cont*num:2}')
        cont += 1
    print('=-='*5)