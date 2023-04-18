lista = list()
while True:
    num = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(num)
    elif num < lista[-1]:
        lista.append(num)
    else:
        posição = 0
        while posição < len(lista):
            if num >= lista[posição]:
                lista.insert(posição, num)
                break
            posição += 1
    resp = str(input('Deseja continuar?[S/N] '))
    if resp in 'Nn':
        break
if 5 in lista:
    print(f'O numero 5 foi digitado!')
else:
    print('O número 5 não foi digitado!')
print(f'Você digitou {len(lista)} números!')
print(f'Os Números digitados foram {lista}')