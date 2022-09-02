viag = int(input('Quantos KM tem a viagem? '))
if viag <= 200:
    print('O Valor a pagar será de R$ {:.2f} '.format(viag*.5))
else:
    print('O valor a pagar será de R$ {:.2f} '.format(viag*.45))