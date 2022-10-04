soma = 0
for c in range (0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
print('A soma dos números pares digitados é {}'.format(soma))