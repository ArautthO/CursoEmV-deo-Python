term = int(input('1º termo da Progressão aritimética: '))
raz = int(input('Digite a sua razão: '))
for c in range(1, 10+1):
    print('{} '.format(term), end='➙')
    term = term + raz
print('ACABOU!')


primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in  range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='->')
print('ACABOU!!')
