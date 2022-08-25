dia = int (input('Quantos dias o carro foi utilizado? '))
km = float (input('Quantos km foram rodados nesse período?'))
valor1 = (dia*60)
valor2 = (km*0.15)
total = valor1+valor2
print('O aluguel de {} dias do carro, e mais o valor de {} km Rodados, resultará em R$ {} a pagar!'.format(dia, km, total))