produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*39)
print(f'{"LISTAGEM DE PREÇOS":^39}')
print('-'*39)
for cont in range (len(produtos)):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<30}', end='')
    else:
        print(f'R${produtos[cont]: >7.2f}')
print('-'*39)