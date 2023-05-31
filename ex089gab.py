boletim = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    med = nota1 + nota2 / 2
    boletim.append([nome, [nota1, nota2], med])
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    quest = int(input('Mostrar notas de qua aluno?(999 interrompe): '))
    if quest == 999:
        break
    if quest <= len(boletim) - 1:
        print(f'Notas de  {boletim[quest][0]} são {boletim[quest][1]}')
print('<<< VOLTE SEMPRE! >>>')