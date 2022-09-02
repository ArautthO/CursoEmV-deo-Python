vel = int(input('Qual a velocidade atual? '))
mult = (vel - 80)* 7
if vel <= 80:
    print('Parabéns você está dentro do limite de velocidade!')
else:
    print('Multado! Você terá de pagar uma multa de R${}'.format(mult))