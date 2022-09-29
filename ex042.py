print('Digite valores de um triângulo:')
lad1 = float(input('-> Lado 1: '))
lad2 = float(input('-> Lado 2: '))
lad3 = float(input('-> lado 3: '))
if lad1 + lad2 > lad3 and lad1 + lad3 > lad2 and lad2 +lad3 > lad1:
    if lad1 == lad2 == lad3:
        print('Esse triângulo é Equilátero, pois é formado por {}, {} e {} que são iguais'.format(lad1, lad2, lad3))
    elif lad1 == lad2 or lad1 == lad3 or lad2 == lad3:
        print('Esse triângulo é Isósceles, pois é formado por {}, {} e {} que são dois lados iguais e um diferente'.format(lad1, lad2, lad3))
    else:
        print('Esse triângulo é Escaleno, pois é formado por {}, {} e {}, que são lados diferentes'.format(lad1, lad2, lad3))
else:
    print('Os lados {}, {} e {} não podem formar um triângulo'.format(lad1, lad2, lad3))
