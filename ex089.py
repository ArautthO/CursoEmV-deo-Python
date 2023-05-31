aluno = list()
boletim = list()
print('Cadastramentos de notas:')
while True:
    nome = str(input('Nome: '))
    aluno.append(nome)
    valor = float(input('Nota 1: '))
    aluno.append(valor)
    valor = float(input('Nota 2: '))
    aluno.append(valor)
    boletim.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
print('=-'*15)
print('Nº   NOME:          MÉDIA')
print('~~'*15)
for c in range(0, len(boletim)):
    print(f'{c:<2}   {boletim[c][0]:<10}   {(boletim[c][1]+boletim[c][2])/2:>5}')
while True:
    quest = int(input('Mostrar notas de qual aluno?(999 para sair) '))
    if quest == 999:
        break
    elif quest >= len(boletim):
        print('ATENÇÃO!!')
        print('Desculpe Digite um número válido!')
        print('###'*12)
    else:
        print(f'As notas de {boletim[quest][0]} são {boletim[quest][1]} e {boletim[quest][2]}')
        print('=-='*12)