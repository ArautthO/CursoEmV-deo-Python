valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Deseja Continuar?[S/N] '))
    if resp in 'Nn':
        break
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        par.append(valores[c])
    else:
        impar.append(valores[c])
print(f'Os valores são {valores}.')
print(f'Os números pares são {par}.')
print(f'Os números ímpares são {impar}.')