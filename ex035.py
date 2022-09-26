lad1 = float(input('Digite um comprimento: '))
lad2 = float(input('Digite outro comprimento: '))
lad3 = float(input('Digite outro comprimento: '))
if lad1 < lad2 + lad3 and lad2 < lad1 + lad3 and lad3 < lad1 + lad2:
    print('As Retas Podem formar um triângulo!')
else:
    print('As Retas não podem formar um triângulo!')
#if lad1 + lad2 > lad3:
#    if lad2 + lad3 > lad1:
#        if lad3 + lad1 > lad2:
#           print('Com essas retas é possivel formar um triângulo!')
#        else:
#            print('Com essas retas não é possível criar um triangulo')
#    else:
#        print('Com essas retas não é possível criar um triângulo!')
#else:
#    print('Com essas retas não é possível criar um triângulo!')
