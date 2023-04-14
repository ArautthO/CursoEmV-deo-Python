cinq = vint = dez = um = valor = rest = 0
print('=-='*9)
print('Bem Vindo ao Banco Mesquita')
print('=-='*9)
valor = int(input('Quanto Quer Sacar? R$ '))
cinq = valor // 50
rest = valor % 50
vint = rest // 20
valor = rest % 20
dez = valor // 10
rest = valor % 10
um = rest // 1
print('=-='*10)
print(f'Total de {cinq} cédulas de R$ 50')
print(f'Total de {vint} cédulas de R$ 20')
print(f'Total de {dez} cédulas de R$ 10')
print(f'Total de {um} cédulas de R$ 1')
print('=-='*10)