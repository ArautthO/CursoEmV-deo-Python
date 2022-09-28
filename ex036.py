casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o valor do seu salário? '))
temp = int(input('Quantas anos pretende pagar? '))
anos = temp * 12
finan = casa / anos

if finan >= sal*.3:
    print('Você terá {} parcelas de R${:.2f}, durante {} anos'.format(anos, finan, temp))
    print('Desculpe, mas você não poderá fincanciar essa casa!')
else:
    print('Parabéns! Seu financiamento foi aprovado!')
    print('Você terá {} parcelas de R${:.2f}, durante {} anos'.format(anos, finan, temp))