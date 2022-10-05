max = 0
min = 0
for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        max = peso
        min = peso
    else:
        if peso > max:
            max = peso
        if peso < min:
            min = peso
print('O maior peso foi {}Kg e o menor foi {}Kg!'.format(max, min))