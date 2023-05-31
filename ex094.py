grupo = list()
pessoa = dict()
soma = med = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:[M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por Favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-=' * 15)
print(f'A) Ao todo são {len(grupo)} pessoas cadastradas.')
med = soma / len(grupo)
print(f'B) A média das idades é {med:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) lista de pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] >= med:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< Até Mais >>')