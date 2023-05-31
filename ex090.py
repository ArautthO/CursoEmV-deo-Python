aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('=-'*25)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
