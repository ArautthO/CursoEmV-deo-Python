from datetime import date
maiores = 0
menores = 0
for c in range(0, 6+1):
    nasc = int(input('Qual a data de nascimento? '))
    if date.today().year - nasc >= 21:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('O total de maiores é {} e de menores é {}'.format(maiores, menores))