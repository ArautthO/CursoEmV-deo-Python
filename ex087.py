matriz = [[], [], []]
par = terceira = maior = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [0, {c}]: '))
    matriz[0].append(num)
for c in range(0, 3):
    num = int(input(f'Digite um valor para [1, {c}]: '))
    matriz[1].append(num)
for c in range(0, 3):
    num = int(input(f'Digite um valor para [2, {c}]: '))
    matriz[2].append(num)
print(matriz)
print('=-='*9)
print(f'[ {matriz[0][0]:^5} ][ {matriz[0][1]:^5} ][ {matriz[0][2]:^5} ]')
print(f'[ {matriz[1][0]:^5} ][ {matriz[1][1]:^5} ][ {matriz[1][2]:^5} ]')
print(f'[ {matriz[2][0]:^5} ][ {matriz[2][1]:^5} ][ {matriz[2][2]:^5} ]')
print('=-='*9)
for c in matriz:
    for m in c:
        if m % 2 == 0:
            par += m
for l in range(0, 3):
    terceira += matriz[l][2]
for c in matriz[1]:
    if c == 0:
        maior = matriz[1][0]
    elif maior <= c:
        maior = c
print(f'A soma dos valores pares são {par}.')
print(f'A soma da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}.')