sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if sex != 'M' and sex != 'F':
        print('Erro esse sexo não existe! Digite novamente!')
if sex == 'M':
    print('Seja bem vindo!')
else:
    print('Seja bem vinda!')