nom = str(input('Digite seu nome: ')).strip()
sobrnm = nom.split()
print('O nome é {}, e o último é {}'.format(sobrnm[0],sobrnm[len(sobrnm)-1]))