pessoas = list()
maiorpeso = list()
maiornom = list()
menorpeso = list()
menornom = list()
while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    resp = str(input('Deseja continuar?[S/N] '))
    if resp in 'Nn':
        break
for c in range(1, len(pessoas), 2):
    if c == 1:
        maiorpeso = pessoas[c:c+1]
        menorpeso = pessoas[c:c+1]
    if maiorpeso[0] < pessoas[c]:
        maiorpeso = pessoas[c:c+1]
        maiornom = pessoas[c-1:c]
    elif maiorpeso[0] == pessoas[c]:
        maiornom.append(pessoas[c-1:c])
    if menorpeso[0] > pessoas[c]:
        menorpeso = pessoas[c:c+1]
        menornom = pessoas[c-1:c]
    elif menorpeso[0] == pessoas[c]:
        menornom.append(pessoas[c-1:c])
print(f'O número de cadastrados foi {len(pessoas)/2}.')
print(f'O maior peso foi {maiorpeso}, peso de {maiornom}.')
print(f'O menor peso foi {menorpeso},  peso de {menornom}.')