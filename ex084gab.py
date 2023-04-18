pessoas = list()
infos = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    if len(infos) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    infos.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Deseja continuar?[S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'O número de cadastrados foi {len(infos)}.')
print(f'O maior peso foi {maior}kg, peso de ', end='')
for p in infos:
    if p[1] == maior:
        print(f' {p[0]}', end='')
print(f'\nO menor peso foi {menor}kg,  peso de ', end='')
for p in infos:
    if p[1] == menor:
        print(f' {p[0]}', end='')