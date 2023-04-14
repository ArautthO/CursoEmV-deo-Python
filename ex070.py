soma = maior = menor = cont = 1
prod = ' '
print('ORGANIZAÇÕES TABAJARA!')
while True:
    nom = str(input('Produto: '))
    valor = float(input('Preço: R$ '))
    cont += 1
    if cont == 0 or valor < menor:
        menor = valor
        prod = nom
    soma += valor
    if valor > 1000:
        maior += 1
    said = ' '
    while said not in 'SN':
        said = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if said == 'N':
        break
print(f'O Total da Compra foi R${soma:.2f}.')
print(f'{maior} deles Custaram mais de R$ 1000.')
print(f'E o mais barato foi o {prod}.')