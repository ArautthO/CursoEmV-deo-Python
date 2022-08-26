num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {}'.format(num))
print('a casa de milhar é {}!'.format(m))
print('a casa da centena é {}!'.format(c))
print('a casa da dezena é {}!'.format(d))
print('a casa da unidade é {}!'.format(u))
