from random import randint
win = 0
while True:
    jogador = int(input('Seu número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print(f'Você jogou {jogador} e o Computador {computador}. Total de {total}')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo =='P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            win += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            win += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos Jogar Novamente...')
print(f'GAME OVER! Você Ganhou {win} vezes consecutivas.')
