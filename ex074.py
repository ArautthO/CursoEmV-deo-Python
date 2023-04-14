from random import randint
maior = menor =0
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for cont in range (0, 5):
    if cont == 0:
        maior = menor = num[cont]
    if num[cont] > maior:
        maior = num[cont]
    if num [cont] < menor:
        menor = num[cont]
print(num)
print(f'O maior número foi {maior}!')
print(f'O menor número foi {menor}!')
