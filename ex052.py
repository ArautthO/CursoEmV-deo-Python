num = int(input('Digite um número: '))
prim = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;32m', end=' ')
        prim = prim + 1
    else:
        print('\033[0;31m', end=' ')
    print('{}'.format(c), end=' ')
if prim == 2:
    print('\n\033[mO número {} foi dividido {} vezes e é um número primo!'.format(num, prim))
else:
    print('\n\033[mO número {} foi dividido {} vezes e não é um número primo!'.format(num, prim))