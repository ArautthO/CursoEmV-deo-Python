import math
'''cata = float(input('Digite o valor do Cateto adjacente: '))
cato = float(input('Digite o valor do cateto oposto: '))
hipo = pow(pow(cata,2)+pow(cato,2),(1/2))
print('O valor a hipotenusa é {:.2f}!'.format(hipo))'''
co = float(input('Digite o valor cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip= math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hip))