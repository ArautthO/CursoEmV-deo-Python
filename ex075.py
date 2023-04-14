print('Digite quatro valores:')
tres = pares = 0
valores = int(input('Primeiro: ')), int(input('Segundo: ')), int(input('Terceiro: ')), int(input('Quarto: '))
print('Apareceram {} números nove'.format(valores.count(9)))
print('O valores pares foram: ', end='')
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        print(valores[c], end=' ')
    if valores[c] == 3:
        tres += 1
if tres == 0:
    print('\nO número 3 não apareceu nenhuma vez!')
else:
    print('\nO número 3 apareceu na {}ª posição !'.format(valores.index(3) + 1))

