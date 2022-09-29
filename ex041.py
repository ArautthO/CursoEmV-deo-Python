from datetime import date
nasc = int(input('Qual o ano em que o atleta nasceu? '))
ano = date.today().year
cat = ano - nasc
if cat <= 9:
    print('A categoria do atleta é Mirim, pois ele tem {} anos!'.format(cat))
elif cat <= 14:
    print('A categoria do atleta é Infantil, pois ele tem {} anos!'.format(cat))
elif cat <= 19:
    print('A categoria do atleta é Junior, pois ele tem {} anos!'.format(cat))
elif cat <= 20:
    print('A categoria do atleta é Sênior, pois ele tem {} anos'.format(cat))
else:
    print('A categoria do atleta é MASTER, pois ele tem {} anos'.format(cat))