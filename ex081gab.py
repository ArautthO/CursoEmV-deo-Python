valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
print(valores)
print(f'Você digitou {len(valores)} elementos!')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O 5 foi digitado!')
else:
    print('Desculpe 5 não foi digitado!')