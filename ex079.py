valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor repetido! não foi adicionado!')
    resp = input('Deseja Continuar?[S/N] ')
    if resp in 'nN':
        break
valores.sort()
print(valores)
