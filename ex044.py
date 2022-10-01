preç = float(input('Digite o Valor do produto: '))
print('Escolha a Forma de Pagamento:')
pag = int(input('*'*22+'\n1 => À Vista \n2 => Cheque \n3 => Cartão à Vista \n4 => Cartão até 2X \n5 => Cartão mais de 3X\n'+'*'*22+'\n'))
if pag == 1:
    print('O total a pagar será R${:.2f} com 10% de desconto!'.format(preç-(preç*10/100)))
elif pag == 2:
    print('O total a pagar será R${:.2f} com 10% de desconto!'.format(preç-(preç*10/100)))
elif pag == 3:
    print('O total a pagar será R${:.2f} com 5% de desconto!'.format(preç-(preç*5/100)))
elif pag == 4:
    print('O Valor a pagar será R${:.2f}, sem acréscimo!'.format(preç))
elif pag == 5:
    print('O Valor a pagar será R${:.2f} com 20% de juros!'.format(preç+(preç*20/100)))
else:
    print('Forma de Pagamento não reconhecida!')