hom = mul = cont = maior = 0
print('Cadastre uma Pessoa:')
while True:
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo[M/F]: ')).strip().upper()[0]
        if sexo in 'M':
            hom += 1
    idad = int(input('Digite a idade: '))
    if idad >= 18:
        maior += 1
    if sexo in 'F' and idad < 20:
        mul += 1
    said = ' '
    while said not in 'SN':
        said = str(input('Deseja continuar? [S/N]')).strip().upper()
    if said in 'N':
        break
print(f'Temos {maior} pessoas maiores de 18 anos')
print(f'Foram {hom} homens cadastrados!')
print(f'E {mul} mulheres menores de 20 anos!')
