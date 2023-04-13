med = 0
nummulheres = 0
hvelho = ''
maioridadeh =0
for c in range(1, 5):
    print('----- {}º PESSOA -----'.format(c))
    nom = str(input('Nome: ')).strip()
    ida = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip()
    med += ida
    if c == 1 and sex in 'Mm':
        maioridadeh = ida
        hvelho = nom
    if sex in 'mM' and ida > maioridadeh:
        maioridadeh = ida
        hvelho = nom
    if sex in 'Ff' and ida < 20:
        nummulheres += +1
print('A média de idade do grupo é {}!'.format(med/4))
print('O homem mais velho  tem {} anos e é o {}!'.format(maioridadeh, hvelho))
print('O número de mulheres menores que 20 anos é {}'.format(nummulheres))