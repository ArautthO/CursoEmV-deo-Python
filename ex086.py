matriz = [[], [], []]
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
print('=-'*8)
print(f'[ {matriz[0][0]:^5} ][ {matriz[0][1]:^5} ][ {matriz[0][2]:^5} ]')
print(f'[ {matriz[1][0]:^5} ][ {matriz[1][1]:^5} ][ {matriz[1][2]:^5} ]')
print(f'[ {matriz[2][0]:^5} ][ {matriz[2][1]:^5} ][ {matriz[2][2]:^5} ]')
print('=-'*8)