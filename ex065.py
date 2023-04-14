from time import sleep
ret = ''
cont = maior = menor = soma = 0
while ret != 'N':
    num = int(input('Digite um número:'))
    if menor == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    soma += num
    ret = str(input('Deseja continuar [S/N]')).upper().strip()
sleep(1)
print('A média entre os números é {}'.format(soma/cont))
sleep(1)
print('O maior número foi {}!'.format(maior))
sleep(1)
print('P menor número foi {}!'.format(menor))