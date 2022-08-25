from math import radians, sin, cos, tan
ang = float(input('Digite o angulo a ser calculado: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print('com o angulo de  {} o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}!'.format(ang, seno, coss, tang))