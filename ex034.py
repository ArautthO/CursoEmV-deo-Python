sal = float(input('Digite o seu salário: '))
if sal <= 1250:
    print('O seu aslário passará a ser {:.2f} com 15% de aumento'.format(sal+(sal*15//100)))
else:
    print('O seu salário passará a ser {:.2f} com 10% de aumento.'.format(sal+(sal*10//100)))
