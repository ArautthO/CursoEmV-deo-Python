num = int(input('Digite um número: '))
for c in range(1, 10+1):
    print('{:2} X {:2} = {:2}'.format(num, c, num*c))