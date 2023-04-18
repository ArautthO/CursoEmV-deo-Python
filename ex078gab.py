numeros = posimenor = posimaior = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print(numeros)
print(f'O maior valor foi {maior} encontrado na posição ', end='')
for v, m in enumerate(numeros):
    if maior in m:
            print(f'{v}... ', end='')
print(f'\nE o menor valor foi {menor} encontrado na posição ', end='')
for v, m in enumerate(numeros):
    if menor in m:
        print(f'{v}... ', end='')