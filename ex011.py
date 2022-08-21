alt = float(input('Qual é a altura da parede? '))
larg = float(input('Qual é a Largura da parede? '))
area = alt*larg
print('Para uma parede de {}m², você vai precisar de {} litros de tinta!'.format(area, area/2))