sexo = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, Digite seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado!'.format(sexo))