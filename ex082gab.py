valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Deseja Continuar?[S/N] '))
    if resp in 'Nn':
        break
for v, c in enumerate(valores):
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Os valores são {valores}.')
print(f'Os números pares são {par}.')
print(f'Os números ímpares são {impar}.')