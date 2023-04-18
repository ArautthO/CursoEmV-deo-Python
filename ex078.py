numeros = posimenor = posimaior = []
for c in range(0, 5):
    numeros.append(input(f'Digite um número para a posição {c}: '))
print(numeros)
print(f'O maior valor foi {max(numeros)} encontrado na posição ', end='')
for v, m in enumerate(numeros):
    if max(numeros) in m:
            print(f'{v}... ', end='')
print(f'\nE o menor valor foi {min(numeros)} encontrado na posição ', end='')
for v, m in enumerate(numeros):
    if min(numeros) in m:
        print(f'{v}... ', end='')
