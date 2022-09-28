not1 = float(input('Digite a primeira nota do aluno: '))
not2 = float(input('Digite a segunda nota do aluno: '))
med = (not1+not2)/2
if med >= 7:
    print('Esse aluno foi aprovado, com nota {}!!'.format(med))
elif med < 5:
    print('Este aluno foi Reprovado, com nota {}!'.format(med))
else:
    print('Este aluno está em recuperação, com nota {}! '.format(med))