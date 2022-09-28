from datetime import date
nasc = int(input('Qual ano você nasceu? '))
ano = date.today().year
alist = nasc + 18
if ano - nasc > 18:
    print('Você já deveria ter se alistado há {} anos, no ano {}!'.format((ano-nasc)-18, alist))
elif ano - nasc < 18:
    print('Você deverá se alistar aos 18 anos, ou seja daqui {} anos!'.format(18-(ano-nasc), alist))
else:
    print('Esse ano , {} Você deve se aprestar às forças armadas brasileira!'.format(alist))