numeros = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(numeros)
numeros[0].sort()
numeros[1].sort()
print(f'Os números digitados foram {numeros}')
print(f'Os pares são {numeros[0]}.')
print(f'Os ímpares são {numeros[1]}.')
