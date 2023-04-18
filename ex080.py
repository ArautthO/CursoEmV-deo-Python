lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'O valor {n} foi inserido na última posição!')
    else:
        posição = 0
        while posição < len(lista):
            if n <= lista[posição]:
                lista.insert(posição, n)
                print(f'O numero {n} foi inserido na posição {posição}!')
                break
            posição += 1
print('=-='*20)
print(f'Os valores digitados em ordem foram {lista}.')